from fastapi import FastAPI, Depends, HTTPException, status, Request, Response, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
import neural_network
import uuid
import os
import shutil



SECRET_KEY = "RkDbB41hUuCVfAj4PA9rpUxtRN3FVocqhCE2moP7EjC1WeRWuD9RvRLujgz9IsLXDnIHf3Jywivjdcx3L02OQA"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

DATABASE_URL = "postgresql://postgres:root@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Files(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    generated_filename = Column(String)
    filename_at_upload = Column(String)
    user = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, index=True)
    phone = Column(String, index=True)
    age = Column(Integer)
    bio = Column(String)

class RevokedToken(Base):
    __tablename__ = "revoked_tokens"

    id = Column(Integer, primary_key=True, index=True)
    jti = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

def db_create():
    Base.metadata.drop_all(bind=engine)
    print("Databases dropped")
    Base.metadata.create_all(bind=engine)
    print("Databases created")

db_create()



from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class PromptText(BaseModel):
    prompt: str
    answers: list

class UserOut(UserBase):
    email: str
    age: int
    bio: str
    name: str

    class Config:
        orm_mode = True

class UserProfileEdit(BaseModel):
    email: str
    name: str
    phone: str
    age: int
    bio: str

class Token(BaseModel):
    access_token: str
    token_type: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    to_encode.update({"jti": str(uuid.uuid4())})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

import uuid  

def is_token_revoked(db: Session, jti: str):
    return db.query(RevokedToken).filter(RevokedToken.jti == jti).first() is not None

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось проверить учетные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("sub"))
        jti: str = payload.get("jti")
        if user_id is None or jti is None:
            raise credentials_exception
        if is_token_revoked(db, jti):
            raise HTTPException(status_code=401, detail="Токен отозван")
    except (JWTError, ValueError):
        raise credentials_exception
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Замените на ваш домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/users/", response_model=UserOut)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = get_user(db, user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
    hashed_password = get_password_hash(user_in.password)
    user = User(email=user_in.email, hashed_password=hashed_password, name="", phone="", age=-1, bio="")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Некорректный email или пароль")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.email)},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=UserProfileEdit)
def read_users_me(request: Request, db = Depends(get_db)):
    access_token = request.cookies.get("access_token")
    if access_token:
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
            user = payload.get("sub")
            user = get_user(db, user)
            return user
        except JWTError:
            return JSONResponse({"authenticated": False}, status_code=401)

@app.post("/logout")
def logout(
    response: Response,
    request: Request,
    db: Session = Depends(get_db)
):
    # Извлекаем access_token из HttpOnly куки
    access_token = request.cookies.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="Токен не найден")

    try:
        # Расшифровываем токен для получения jti
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        jti: str = payload.get("jti")
        if not jti:
            raise HTTPException(status_code=400, detail="Некорректный токен")
        
        # Добавляем токен в базу отозванных токенов
        revoked_token = RevokedToken(jti=jti)
        db.add(revoked_token)
        db.commit()
        
        # Удаляем куку access_token
        response.delete_cookie(key="access_token", httponly=True, samesite="lax")
        
        return {"msg": "Вы успешно вышли из аккаунта"}
    except JWTError:
        raise HTTPException(status_code=400, detail="Некорректный токен")



@app.get("/auth/status")
async def auth_status(request: Request):
    access_token = request.cookies.get("access_token")
    if access_token:
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
            user = {"id": payload.get("sub"), "name": payload.get("name")}
            return {"authenticated": True, "user": user}
        except JWTError:
            return JSONResponse({"authenticated": False}, status_code=401)
    else:
        return JSONResponse({"authenticated": False}, status_code=401)

@app.post("/neural_network")
def neural_network_access(prompt: PromptText):
    try:
        return { "message": neural_network.get_answer(str(prompt.prompt), prompt.answers)["choices"][0]["message"]["content"] }
    except Exception as e:
        return { "message": f"An error occured: {e}" }

@app.post("/login")
def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Некорректный email или пароль")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.email)},
        expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  
        samesite="lax"
    )
    return {"message": "Вы успешно вошли в систему"}

@app.post("/profileEdit")
def profile_edit(user_info: UserProfileEdit, db: Session = Depends(get_db)):
    user = get_user(db, user_info.email)
    user.name = user_info.name
    user.age = user_info.age
    user.email = user_info.email
    user.bio = user_info.bio
    user.phone = user_info.phone
    db.commit()  

@app.post("/upload")
async def upload_file(file: UploadFile, request: Request, db = Depends(get_db)):
    try:
        access_token = request.cookies.get("access_token")
        file_format = file.filename.split(".")[-1]
        filename = str(uuid.uuid4())
        file_path = os.path.join("imgs", filename + "." + file_format)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
        user = payload.get("sub")
        db.add(Files(generated_filename=f"{filename}.{file_format}", filename_at_upload=f"{file.filename}", user=user))
        db.commit()
        db.close()
        return f"{filename}.{file_format}"
    except Exception as e:
        return { "error": f"An error has occured: {e}"}
    
@app.get("/download_all_by_email")
async def files_by_email(request: Request, db = Depends(get_db)):
    access_token = request.cookies.get("access_token")
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
        user = payload.get("sub")
        files = db.query(Files).filter(Files.user == user).all()
        return files
    except Exception as e:
        return {"error": f"An error has occured: {e}"}

@app.get("/download/{file_path:str}")
async def get_file(file_path: str):
    try:
        return FileResponse("imgs/" + file_path)
    except Exception as e:
        return { "error": "An error has occured: {e}"}