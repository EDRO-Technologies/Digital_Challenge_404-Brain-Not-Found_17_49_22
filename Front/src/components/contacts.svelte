<script>
    import Header from "./Header.svelte";

    const contacts = [
        {
            name: "Иван Иванов",
            position: "Директор",
            email: "ivan.ivanov@example.com",
            phone: "+7 (123) 456-78-90"
        },
        {
            name: "Мария Петрова",
            position: "Маркетолог",
            email: "maria.petrova@example.com",
            phone: "+7 (123) 456-78-91"
        },
        {
            name: "Сергей Сидоров",
            position: "Разработчик",
            email: "sergey.sidorov@example.com",
            phone: "+7 (123) 456-78-92"
        },
        {
            name: "Анна Смирнова",
            position: "Дизайнер",
            email: "anna.smirnova@example.com",
            phone: "+7 (123) 456-78-93"
        }
    ];
</script>

<Header />

<style>
    .contacts-page {
        background-color: #f9f9f9;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 800px; /* Увеличиваем ширину для колонок */
        margin: 40px auto;
        font-family: Arial, sans-serif;
        display: flex; /* Используем Flexbox */
        flex-wrap: wrap; /* Позволяем элементам переноситься на новую строку */
        justify-content: space-between; /* Распределяем пространство между колонками */
    }

    h2 {
        text-align: center;
        margin-bottom: 30px;
        color: #333;
        width: 100%; /* Заголовок занимает всю ширину */
        font-size: 22px;
    }

    .contact {
        background: white;
        border-radius: 8px;
        padding: 15px;
        margin: 10px; /* Уменьшаем отступы между контактами */
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
        flex: 0 0 calc(50% - 20px); /* Устанавливаем ширину каждого контакта на 50% минус отступы */
        box-sizing: border-box; /* Учитываем отступы в ширине */
    }

    .contact:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .contact h3 {
        margin: 0;
        font-size: 20px;
        color: #007BFF;
    }

    .contact p {
        margin: 5px 0;
        font-size: 14px;
        color: #555;
    }

    .contact strong {
        color: #333;
    }
</style>

<div class="contacts-page">
    <h2>Контакты</h2>
    {#each contacts as contact}
        <div class="contact">
            <h3>{contact.name}</h3>
            <p><strong>Должность:</strong> {contact.position}</p>
            <p><strong>Email:</strong> <a href={`mailto:${contact.email}`}>{contact.email}</a></p>
            <p><strong>Телефон:</strong> <a href={`tel:${contact.phone}`}>{contact.phone}</a></p>
        </div>
    {/each}
</div>
