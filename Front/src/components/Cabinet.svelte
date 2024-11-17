<script>
    import { onMount } from "svelte";
    let user = {
        name: "",
        email: "",
        phone: "",
        age: null,
        bio: ""
    };
    let file;
    let files = [];
    let validFiles = []
    let achievements = [];
    let newAchievement = "";
    let message = "";
    let activeSection = 'info';
    let editMode = false;
    let editButtonText = "Редактировать"

    async function uploadFile() {
        if (!file) {
            return;
        }

        const formData = new FormData()
        formData.append("file", file);

        try {
            const response = await fetch("http://localhost:8000/upload", {
                method: "POST",
                credentials: "include",
                body: formData
            })
            let data = await response.json()
            console.log(data)
        } catch (e) {
            console.log(e)
        }
    }

    onMount(async () => {
        try {
            let response = await fetch("http://localhost:8000/users/me", {
                credentials: "include",
                method: "GET"
            })
            if (response.ok) {
                let data = await response.json()
                user.name = data.name
                user.email = data.email
                user.phone = data.phone
                user.age = data.age
                user.bio = data.bio
            }
        } catch(e) {
            console.log(e)
        }
        try {
            let response = await fetch("http://localhost:8000/download_all_by_email", {
                credentials: "include",
                method: "GET",
            })
            if (response.ok) {
                let data = await response.json()
                console.log(data)
                for(let i = 0; i < data.length; i++) {
                    files.push(data[i].filename_at_upload)
                }
                console.log(files)
            }
        } catch(e) {
            console.log(e)
        }
    })

    const acceptedFileTypes = ["image/jpeg", "image/png", "application/pdf"];

    function validateFile(file) {
        if (!acceptedFileTypes.includes(file.type)) {
            message = "Только файлы форматов JPEG, PNG и PDF разрешены.";
            return false;
        }
        return true;
    }
    function handleFileUpload(event) {
    file = event.target.files[0];
    if (!file) {
        message = "Файл не выбран!";
        return;
    }

    if (validateFile(file)) {
        message = `Выбран файл: ${file.name}`;
    } else {
        message = "Некорректный формат файла.";
        file = null;
    }
}

    function removeFile(fileToRemove) {
        files = files.filter(file => file !== fileToRemove);
    }

    function addAchievement() {
        if (newAchievement.trim() !== "") {
            achievements.push(newAchievement);
            newAchievement = "";
            message = "Достижение успешно добавлено!";
        } else {
            message = "Введите достижение для добавления.";
        }
    }

    function removeAchievement(achievementToRemove) {
        achievements = achievements.filter(achievement => achievement !== achievementToRemove);
    }

    function setActiveSection(section) {
        activeSection = section; 
    }

    let editProfile = async () => {
        editMode = !editMode
        editButtonText = editMode ? "Сохранить" : "Редактировать"
        if (!editMode) {
            try {
                let response = await fetch("http://localhost:8000/profileEdit", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                        },
                    body: JSON.stringify({
                        "email": user.email,
                        "name": user.name,
                        "phone": user.phone,
                        "age": user.age,
                        "bio": user.bio
                    })
                })
            } catch (e) {
                console.log(e)
            }
        }
    }
</script>

<style>
    * {
        box-sizing: border-box;
    }

    body {
        display: flex;
        margin: 0;
        background-color: #f2f3f7;
        font-family: Arial, sans-serif;
    }

    .sidebar {
        width: 200px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        position: fixed;
        height: 100%;
        padding: 20px;
        overflow-y: auto;
        border-right: 1px solid #e1e1e1;
    }

    .sidebar h2 {
        margin-top: 0;
        font-size: 1.2rem;
        color: #333;
    }

    .sidebar ul {
        list-style: none;
        padding: 0;
    }

    .sidebar ul li {
        margin: 10px 0;
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background-color 0.3s;
    }

    .sidebar ul li:hover {
        background-color: #f2f2f2;
    }

    .sidebar ul li.active {
        background-color: #d9d9d9;
    }

    .content {
        margin-left: 220px;
        padding: 40px;
        width: calc(100% - 220px);
    }

    .info-item {
        margin: 5px 0;
    }
    .info-item p {
        height: 29.6px;
    }
    input[type="file"], input[type="text"] {
        display: block;
        margin: 20px auto;
        padding: 10px;
        border-radius: 5px;
        background-color: #fafafa;
        border: 1px solid #ccc;
        width: 100%;
    }

    .message {
        text-align: center;
        color: #0ba00b;
        font-weight: bold;
        margin: 10px 0;
    }

    .file-list, .achievement-list {
        list-style-type: none;
        padding: 0;
    }

    .file-item, .achievement-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f9f9f9;
        padding: 10px 15px;
        border-radius: 5px;
        margin: 5px 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .file-item:hover, .achievement-item:hover {
        background-color: #e9e9e9;
        transition: background-color 0.2s ease;
    }

    .remove-button {
        cursor: pointer;
        background-color: #08a549;
        border: none;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        transition: background-color 0.3s;
    }

    .remove-button:hover {
        background-color: #992f0b;
    }
    .editButton {
        padding: 5px;
        border-radius: 10px;
        border: 1px solid;
        border-color: #007FFF;
        min-width: 120px;
    }
    .editButton p {
        transform: translateY(-7%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    input {
        width: 300px;
        border-radius: 5px;
        border: 1px solid;
        padding: 2px;
        padding-left: 5px;
    }
    @media (max-width: 700px) {
        .sidebar {
            width: 100%;
            position: relative;
            height: auto;
        }

        .content {
            margin-left: 0;
            width: 100%;
        }
    }
</style>

<div class="sidebar">
    <h2>Меню</h2>
    <ul>
        <li class={activeSection === 'info' ? 'active' : ''} on:click={() => setActiveSection('info')}>Личная информация</li>
        <li class={activeSection === 'files' ? 'active' : ''} on:click={() => setActiveSection('files')}>Загруженные файлы</li>
        <li class={activeSection === 'achievements' ? 'active' : ''} on:click={() => setActiveSection('achievements')}>Достижения</li>
    </ul>
</div>

<div class="content">
    {#if activeSection === 'info'}
        <div class="personal-info">
            <h2>Личная информация</h2>
        {#if !editMode}
            <div class="info-item"><strong>Имя:</strong><br /><p>{user.name == "" ? "Не введено" : user.name}</p></div>
            <div class="info-item"><strong>Email:</strong><br /><p>{user.email == "" ? "Не введено" : user.email}</p></div>
            <div class="info-item"><strong>Телефон:</strong><br /><p>{user.phone == "" ? "Не введено" : user.phone}</p></div>
            <div class="info-item"><strong>Возраст:</strong><br /><p>{user.age != -1 ? user.age : "Не введено"}</p></div>
            <div class="info-item"><strong>О себе:</strong><br /><p>{user.bio == "" ? "Не введено" : user.bio}</p></div>
        {:else}
            <div class="info-item"><strong>Имя:</strong><br /><input bind:value={user.name}/></div>
            <div class="info-item"><strong>Email:</strong><br /><input bind:value={user.email}/></div>
            <div class="info-item"><strong>Телефон:</strong><br /><input bind:value={user.phone}></div>
            <div class="info-item"><strong>Возраст:</strong><br /><input bind:value={user.age}></div>
            <div class="info-item"><strong>О себе:</strong><br /><input bind:value={user.bio}></div>
        {/if}

        </div>
        <button class="editButton" on:click={editProfile}><p>{editButtonText}</p></button>
    {:else if activeSection === 'files'}
        <h2>Загруженные файлы:</h2>
        <input type="file" bind:this={file} on:change={handleFileUpload} />
        <button on:click={uploadFile}>Загрузить</button>
        {#if message}
            <p class="message">{message}</p>
        {/if}

        <ul class="file-list">
            {#each files as file}
                <li class="file-item">
                    {file}
                    <!-- <button class="remove-button" on:click={() => removeFile(file)}>Удалить</button> -->
                </li>
            {/each}
        </ul>
    {:else if activeSection === 'achievements'}
        <h2>Добавить достижение:</h2>
        <input type="text" bind:value={newAchievement} placeholder="Введите ваше достижение" />
        <button class="remove-button" on:click={addAchievement}>Добавить</button>

        <h2>Ваши достижения:</h2>
        <ul class="achievement-list">
            {#each achievements as achievement}
                <li class="achievement-item">
                    {achievement}
                    <button class="remove-button" on:click={() => removeAchievement(achievement)}>Удалить</button>
                </li>
            {/each}
        </ul>
    {/if}
</div>
