<header>
  
    <style>
      .header {
        background-color: #333;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
      }
    
      .logo img {
        height: 40px;
      }
    
      .nav {
        list-style: none;
        display: flex;
        position: relative;
      }
    
      .nav li {
        margin: 0 15px;
        position: relative;
      }
    
      .nav a {
        color: white;
        text-decoration: none;
        padding: 8px 12px; 
        border-radius: 5px; 
        transition: background-color 0.3s; 
      }
  
      .nav a:hover {
        background-color: rgba(255, 255, 255, 0.2);
      }
  
      .dropdown {
        display: none;
        position: absolute;
        background-color: #444;
        border-radius: 5px;
        padding: 10px 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        z-index: 2;
      }
  
      .nav li:hover .dropdown {
        display: block;
      }
  
      .dropdown a {
        display: block;
        color: white;
        text-decoration: none;
        padding: 8px 12px; 
        transition: background-color 0.3s; 
      }
  
      .dropdown a:hover {
        background-color: rgba(255, 255, 255, 0.3); 
      }
  
      .auth-buttons {
        display: flex;
        gap: 10px;
      }
  
      .auth-button {
        background-color: transparent;
        color: white;
        border: 1px solid white;
        padding: 5px 10px;
        border-radius: 5px;
        text-decoration: none;
        transition: background-color 0.3s, color 0.3s;
      }
  
      .auth-button:hover {
        background-color: white;
        color: #333;
      }
    </style>
    
    <header class="header">
      <div class="logo">
        <img src="logo.png" alt="Логотип компании" />
      </div>
      <nav>
        <ul class="nav">
          <li><a href="/">Главная</a></li>
          <li>
            <a>Меры поддержки</a>
            <div class="dropdown">
              <a href="/federationsupp">Федеральные меры поддержки</a>
              <a href="/regionalsupp">Региональные меры поддержки</a>
            </div>
          </li>
          <li><a href="/about">О нас</a></li>
          <li><a href="/navzlet">"На взлёт!"</a></li>
          <li><a href="/contacts">Контакты</a></li>
        </ul>
      </nav>
      <div class="auth-buttons">
        <a href="/" class="auth-button">Выход</a>
        <a href="/cabinet" class="auth-button">Личный кабинет</a>
      </div>  
    </header>
  </header>
  