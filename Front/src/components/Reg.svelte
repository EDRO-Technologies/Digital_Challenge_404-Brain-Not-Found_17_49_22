    <script>
        import { isAuthenticated } from "../store.js";
        import { onMount } from "svelte";
        onMount( async () => {
            try {
                let response = await fetch("http://localhost:8000/auth/status", {
                    credentials: "include",
                });
                if (response.ok) {
                    const data = await response.json();
                    isAuthenticated.set(data.authenticated);
                } else {
                    isAuthenticated.set(false);
                }
                if ($isAuthenticated) {
                    window.location.href = "/"
                }
            } catch(e) {
                console.log(e);
            }
        })
        let email = '';
        let password = '';
        let confirmPassword = '';
        let passwordConfirmed = true;
        import Header from "./Header.svelte";
        import Footer from "./Footer.svelte";
        let Register = async () => {
            if (password == confirmPassword) {
                let response = await fetch("http://localhost:8000/users", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    },
                    body: JSON.stringify({
                        "email": email,
                        "password": password,
                    })
                })
                let data = await response.json();
                console.log(data)

                const formData = new FormData();
                formData.append('username', email);
                formData.append('password', password);
                response = await fetch("http://localhost:8000/login", {
                    credentials: "include",
                    method: "POST",
                    body: formData
                })
                if (response.ok) {
                    let data = await response.json();
                    console.log(data);
                    window.location.href = "/cabinet";
                }
            } else {
                passwordConfirmed = false;
            }
        }
    </script>
    <Header />

    <style>
        .registration-form {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px; /* Максимальная ширина формы */
            margin: 0 auto; /* Центрируем форму по горизонтали */
            margin-top: 30px;
            margin-bottom: 20px;
        }

        h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
        }

        input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: black; /* Черный цвет кнопки */
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s; /* Плавный переход цвета */
        }

        button:hover {
            background-color: #333; /* Темнее черного при наведении */
        }

        .error {
            color: red;

            font-size: 12px;
            margin-top: 5px;
        }
    </style>

    <div class="registration-form">
        <h2>Регистрация</h2>
        <form>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" bind:value={email} required />
            </div>
            <div class="form-group">
                <label for="password">Пароль:</label>
                <input type="password" id="password" bind:value={password} required />
            </div>
            <div class="form-group">
                <label for="confirmPassword">Подтвердите пароль:</label>
                <input type="password" id="confirmPassword" bind:value={confirmPassword} required />
            </div>
            {#if !passwordConfirmed}
            <div class="error">Пароли не совпадают!</div>
            {/if}
            <button type="submit" on:click={Register}>Зарегистрироваться</button>
        </form>
    </div>
    <Footer isMainPage="true"/>