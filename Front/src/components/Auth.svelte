<script>
    let email = '';
    let password = '';
    import Header from "./Header.svelte";
    import Footer from "./Footer.svelte";
    import { isAuthenticated } from "../store.js";
    import { onMount } from "svelte";
    let loggedIn = false;
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
    let Auth = async () => {
        try {
            const formData = new FormData();
            formData.append('username', email);
            formData.append('password', password);
            let response = await fetch("http://localhost:8000/login", {
                credentials: "include",
                method: "POST",
                body: formData
            })
            if (response.ok) {
                loggedIn = true;
                let data = await response.json();
                console.log(data, loggedIn);
                window.location.href = "/cabinet";
            }

        } catch (e) {
            console.log(e);
        }
    }
</script>
<Header />
<style>
    .login-form {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 400px;
        margin: 0 auto; 
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
        background-color: black; 
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s; 
    }

    button:hover {
        background-color: #333; 
    }

    .error {
        color: red;
        font-size: 12px;
        margin-top: 5px;
    }
</style>

<div class="login-form">
    <h2>Вход</h2>
    <form>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" bind:value={email} required />
        </div>
        <div class="form-group">
            <label for="password">Пароль:</label>
            <input type="password" id="password" bind:value={password} required />
        </div>
        <button type="submit" on:click={Auth}>Войти</button>
    </form>
</div>
<Footer isMainPage="true"/>