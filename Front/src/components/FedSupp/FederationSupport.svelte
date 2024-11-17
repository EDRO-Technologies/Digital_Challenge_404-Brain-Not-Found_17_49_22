<script>
	import Header from '../Header.svelte';
	import Footer from '../Footer.svelte';

  let selectedMeasure = null;

  const measures = [
    {
      title: "Налоговые льготы",
      description: "Для поддержки ИТ-компаний в отдельных сферах бизнеса государство снижает их налоговую нагрузку — переносит сроки уплаты налогов, вводит льготные ставки, устраивает налоговые каникулы.",
      image: "images/налоговые льготы.jpg",
      overlayText: `
				<p>Кому предназначена мера:</p>
				<ul>
					<li>◆ Поддержка малых ИТ-компаний.</li>
					<li>◆ Налоговые каникулы до 3 лет.</li>
				</ul>
        <p style="margin-top: 3%">Виды налогов:</p>
				<ul>
					<li>◆ Налог на прибыль.</li>
					<li>◆ НДС.</li>
          <li>◆ Страховые взносы.</li>
          <li>◆ УСН.</li>
          <li>◆ Налог на имущество и арендные ставки.</li>
          <li>◆ Земельный налог.</li>
				</ul>
        <p style="margin-top: 3%">Получатели:</p>
				<ul>
					<li>◆ Льготы для малого бизнеса.</li>
					<li>◆ Льготы для разработчиков ПО.</li>
          <li>◆ Льготы для дизайн-центров.</li>
				</ul>
        <p style="margin-top: 3%">Подробнее по ссылке: <a style="color: #0D4CD3" href="https://www.gosuslugi.ru/itindustry/tax_incentives">https://www.gosuslugi.ru/itindustry/tax_incentives</a></p>
			`
    },
    {
      title: "Льготные кредиты",
      description: "Государство предоставляет компаниям кредиты по льготной ставке для разработки и внедрения различных, в том числе дорогостоящих ИТ‑решений, а также на покрытие расходов по операционной деятельности.",
      image: "images/льготные кредиты.jpg",
    },
    {
      title: "Гранты",
      description: "Разные программы грантовой поддержки рассчитаны на разные категории получателей — от ИТ‑стартапов до крупных компаний, разрабатывающих или внедряющих отечественные ИТ‑решения.",
      image: "images/гранты.jpg",
    },
    {
      title: "Субсидирование приобретения ПО для МСП",
      description: "Субъекты малого и среднего бизнеса могут приобрести российское ПО со скидкой50%. Список ПО постоянно пополняется.",
      image: "images/субсидирование.jpg",
    },
    {
      title: "Льготная ипотека",
      description: "Оформить льготную ипотеку могут сотрудники ИТ‑организаций, аккредитованных Минцифры.",
      image: "images/ипотека.jpeg",
    },
    {
      title: "Отсрочка от призыва",
      description: "Услуга поможет сотрудникам аккредитованных ИТ‑компаний получить отсрочку от призыва.",
      image: "images/отсрочка.jpg",
    },
    {
      title: "Освобождение от проверок",
      description: "Аккредитованные ИТ-компании освобождены от проведения государственных и муниципальных проверок до конца года. Это снизит административные издержки бизнеса и позволит сконцентрироваться на решении основных задач..",
      image: "images/освобождение.jpg",
    },
    {
      title: "Трудоустройство и ВНЖ для иностранцев",
      description: "Упрощенные процедуры трудоустройства и получения вида на жительство для иностранных IT-специалистов.",
      image: "images/трудоустр.jpg",
    },
    {
      title: "Включение в реестры",
      description: "Российские ИТ-разработчики могут получить государственные меры поддержки. Для этого необходимо включить сведения о программных продуктах в Единый реестр российских программ для ЭВМ и баз данных.",
      image: "images/реестр.jpg",
    },
    {
      title: "Аккредитация",
      description: "ИТ-компании могут получить государственные меры поддержки. Для этого необходимо пройти аккредитацию в Минцифры, после чего компания будет добавлена в реестр аккредитованных ИТ-компаний. Аккредитация ИТ-компаний проводится бесплатно. Подать заявление можно на Госуслугах — его рассмотрят за 15 рабочих дней.",
      image: "images/аккредитация.jpg",
    },
    {
      title: "ИТ-образование",
      description: "Минцифры запустило проект «Цифровые профессии». 75 тыс. человек смогут получить образование в области ИТ со скидкой от 50% до 100%.",
      image: "images/образование.jpg",
    },
    {
      title: "Привлечение финансирования",
      description: "Мера позволит упростить выход ИТ-компаний на Московскую биржу для привлечения капитала и решит вопрос софинансирования частных венчурных технологических фондов для поддержки стартапов.",
      image: "images/финансирование.jpg",
    },
    {
      title: "Поддержка особо значимых проектов",
      description: "Минцифры объявляет о начале приёма заявок на включение в перечень особо значимых проектов, направленных на замещение зарубежных ИТ‑решений.",
      image: "images/поддержка.jpg",
    }
  ];

  function openOverlay(measure) {
		selectedMeasure = measure;
	}

	function closeOverlay() {
		selectedMeasure = null;
	}
</script>

<style>
  .container {
    max-width: 1200px; /* Максимальная ширина контейнера */
    margin: 0 auto; /* Центрирование контейнера */
    padding: 30px 20px; /* Отступ для контейнера */
    display: grid; /* Используем сетку */
    grid-template-columns: repeat(4, 1fr); /* 4 равные колонки */
    gap: 20px; /* Промежутки между элементами */
    border-radius: 10px; /* Закругления контейнера */
    background-color: rgba(99, 125, 173, 0.26); /* Фон контейнера */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Тень для контейнера */
  }

  h1 {
    text-align: center;
    margin-bottom: 30px;
    font-size: 2em; /* Увеличенный размер */
    font-weight: bold; /* Полужирное начертание заголовка */
    color: #ffffff; /* Цвет заголовка */
    padding: 10px;
    background: linear-gradient(270deg, #3c4c6f, #6292a3, #3c4c6f); /* Градиент фона (синий и голубой) */
    background-size: 400% 400%; /* Увеличиваем размер градиента для анимации */
    animation: gradientAnimation 5s ease infinite; /* Анимация градиента */
    border-radius: 0 0 10px 10px; /* Закругление углов заголовка */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2); /* Тень для заголовка */
  }

  @keyframes gradientAnimation {
    0% {
      background-position: 0% 50%; /* Начальная позиция фона */
    }
    50% {
      background-position: 100% 50%; /* Позиция фона в середине анимации */
    }
    100% {
      background-position: 0% 50%; /* Конечная позиция фона */
    }
  }

  .measure {
    border-radius: 10px; /* Закругленные углы карточек */
    overflow: hidden; /* Скрывать переполнение */
    background-color: #ffffff; /* Белый фон для карточек */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Тень для карточек */
    transition: transform 0.3s; /* Плавный эффект при изменении масштаба */
    position: relative; /* Для абсолютного позиционирования заголовка */
    padding: 15px; /* Внутренние отступы карточки */
    text-align: center; /* Выравнивание текста по центру */
    border: 1px solid #e0e0e0; /* Легкая граница вокруг карточек */
    display: flex; /* Использование flexbox для внутреннего размещения элементов */
    flex-direction: column; /* Располагаем элементы вертикально */
    height: 100%; /* Выравнивание карточек по высоте */
  }

  .measure:hover {
    transform: scale(1.05); /* Увеличение карточки при наведении */
  }

  img {
    width: 100%; /* Растягиваем на всю ширину контейнера */
    height: 150px; /* Устанавливаем фиксированную высоту для всех изображений */
    object-fit: cover; /* Обрезка изображения для заполнения блока */
    border-bottom: 4px solid rgb(60, 76, 111); /* Цветовая граница снизу изображения */
    transition: filter 0.3s; /* Плавный переход между эффектами */
  }

  .measure:hover img {
    filter: brightness(70%); /* Затемнение изображения при наведении */
  }

  .measure h2 {
    margin: 5px auto; /* Убираем верхний отступ и минимизируем отступы, чтобы заголовок был ближе к изображению */
    font-size: 1.4em; /* Размер шрифта заголовка */
    color: #3c4c6f; /* Цвет текста заголовка */
    font-weight: bold; /* Полужирный текст */
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Тень для текста заголовка */
    display: flex; /* Используем flex для выравнивания по вертикали */
    justify-content: center; /* Центрируем текст по горизонтали */
    align-items: center; /* Центрируем текст по вертикали */
  }

  .measure p {
    font-size: 0.95em; /* Размер шрифта для описания */
    color: #555; /* Цвет текста описания */
    line-height: 1.5; /* Высота строки для лучшей читаемости */
    margin: 0; /* Убираем отступы */
  }

  .overlay {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background-color: rgba(0, 0, 0, 0.7);
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 3; /* Убедитесь, что оверлей выше остальных элементов */
	}

	.overlay-content {
		background: #ffffff;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
		position: relative;
		width: 80%;
		max-width: 600px;
	}

	.close-button {
		position: absolute;
		top: 10px;
		right: 10px;
		cursor: pointer;
    color: #3c4c6f; /* Синий цвет для текста кнопки */
    background: none; /* Убираем фон кнопки */
	}
</style>

<Header />
<h1>Федеральные меры поддержки в сфере IT</h1>
<div class="container">
	{#each measures as measure}
		<button class="measure" on:click={() => openOverlay(measure)} aria-label={measure.title}>
			<img src={measure.image} alt={measure.title} />
			<h2>{measure.title}</h2>
			<p>{measure.description}</p>
		</button>
	{/each}
</div>

{#if selectedMeasure}
	<div class="overlay" role="dialog" aria-labelledby="overlay-title" aria-modal="true" on:click={closeOverlay}>
		<div class="overlay-content" on:click|stopPropagation>
			<button class="close-button" on:click={closeOverlay} aria-label="Закрыть оверлей">⨉</button>
			<h2 style="color: #0D4CD3; font-weight: bold" id="overlay-title">{selectedMeasure.title}</h2>
			{@html selectedMeasure.overlayText} <!-- Здесь используется вставка HTML -->
		</div>
	</div>
{/if}
<Footer />