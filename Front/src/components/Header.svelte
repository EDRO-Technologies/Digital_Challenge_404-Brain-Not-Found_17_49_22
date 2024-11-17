<script>
  import { isAuthenticated } from "../store.js";
  import { onMount } from "svelte";
  let isLogged = false;
  onMount( async () => {
    try {
      let response = await fetch("http://localhost:8000/auth/status", {
        credentials: "include",
      });
      if (response.ok) {
        const data = await response.json();
        isLogged = data.authenticated;
        isAuthenticated.set(isLogged);
      } else {
        isAuthenticated.set(false);
      }
    } catch(e) {
      console.log(e);
    }
  })
  let logout = async () => {
    try {
      let response = await fetch("http://localhost:8000/logout", {
        method: "POST",
        credentials: "include"
      })
      if (response.ok) {
        const data = await response.json()
        console.log(data)
        window.location.href = "/";
      }
    } catch (e) {
      console.log(e)
    }
  }
</script>

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
      height: 50px;
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
      background-color: #333;
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
      <img src="logo.svg" alt="">
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
        <li><a href="/navzlet">"На взлёт!"</a></li>
        <li><a href="/contacts">Контакты</a></li>
      </ul>
    </nav>
    <div class="auth-buttons">
{#if isLogged}
      <a href="/cabinet" class="auth-button">Личный кабинет</a>
      <a href="/" class="auth-button" on:click={logout}>Выход</a>
{:else}
<a href="/auth" class="auth-button">Вход</a>
      <a href="/reg" class="auth-button">Регистрация</a>
{/if}
    </div>  
  </header>
</header>
