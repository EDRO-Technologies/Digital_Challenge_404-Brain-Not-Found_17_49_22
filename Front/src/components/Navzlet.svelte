<script>
  let goal = "";
  let parsedData = [];
  let buttonVisible = true;
  let questions = [
    {
      question: "Что для вас наиболее важно в работе?",
      options: ["Карьера", "Деньги", "Развитие", "Команда"]
    },
    {
      question: "Какой навык вы хотите развить?",
      options: ["Программирование", "Коммуникации", "Управление проектами", "Дизайн"]
    },
    {
      question: "Что вас мотивирует?",
      options: ["Новые вызовы", "Признание", "Финансовая стабильность", "Забота о людях"]
    }
  ];

  let userAnswers = Array(questions.length).fill(null);
  let goals = [];
  
  async function getGoals() {
    buttonVisible = false;
    goals = [];
    userAnswers.forEach((answer, index) => {
      if (answer) {
        goals.push(`Развивайте навык: ${answer}`);
      }
    });
    try {
      let response = await fetch("http://localhost:8000/neural_network", {
        method: "POST", 
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          prompt: goal,
          answers: userAnswers
        })
      })
      let data = await response.json();
      console.log(data)
      console.log(data.message)
      parsedData = parseGoals(data.message);
      console.log(parsedData)
    } catch(e) {
      console.log(e);
    }
  }

  function parseGoals(text) {
    const regex = /\[(goal|subgoal)\](.*?)\[\/\1\]/gs;
    const matches = [...text.matchAll(regex)];
    const result = [];
    let currentGoal = null;

    for (const match of matches) {
        const [fullMatch, tag, content] = match;
        const trimmedContent = content.trim();

        if (tag === 'goal') {
            currentGoal = [trimmedContent, []];
            result.push(currentGoal);
        } else if (tag === 'subgoal') {
            if (currentGoal) {
                currentGoal[1].push(trimmedContent);
            }
        }
    }

    return result;
  }
</script>

<style>
body {
  font-family: 'Arial', sans-serif;
  background: linear-gradient(to right, #ffcccc, #ffffff);
  color: #333;
}

.container {
  max-width: 900px;
  margin: auto;
  text-align: center;
  margin-top: 40px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

h1 {
  font-size: 28px;
  color: darkred;
  margin-bottom: 20px;
}

.question {
  margin: 20px 0;
  font-size: 1.2em;
  font-weight: bold;
  color: #444;
  background-color: #9151516d;
  padding: 12px;
  border-radius: 5px;
}

.option {
  margin: 10px 0;
  background-color: #efefefbb;
  padding: 12px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.option:hover {
  background-color: #d6d6d6;
}

.option.selected {
  background-color: #1e90ff;
  color: white;
}

.input-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

input {
  border: 1px solid #ccc;
  border-radius: 7px 0 0 7px;
  padding: 10px;
  flex-grow: 1;
  font-size: 1em;
}

button {
  padding: 10px 20px;
  background-color: #96d495;
  color: white;
  border: none;
  border-radius: 0 7px 7px 0;
  cursor: pointer;
  font-size: 1.2em;
  transition: background-color 0.3s;
}

button:hover {
    background-color: rgb(92, 203, 100);
  }

  .goals {
    margin-top: 30px;
    text-align: left;
  }

  ul {
    list-style: circle;
    padding-left: 20px;
  }

  ul ul {
    list-style: inside;
    padding-left: 10px;
  }

  li {
    margin: 5px 0;
  }

  h1 {
    text-align: center;
    margin-bottom: 30px;
    font-size: 2em;
    font-weight: bold; 
    color: #ffffff;
    padding: 10px;
    background: linear-gradient(270deg, #5d3e3e, #a36262, #5d3e3e); 
    background-size: 400% 400%; 
    animation: gradientAnimation 5s ease infinite; 
    border-radius: 10px; 
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  }

  @keyframes gradientAnimation {
    0% {
      background-position: 0% 50%; 
    }
    50% {
      background-position: 100% 50%; 
    }
    100% {
      background-position: 0% 50%;
    }
  }
</style>

<div class="container">
  <h1>На взлёт!</h1>
  <p>Ответьте на вопросы, чтобы выстроить индивидуальную траекторию.</p>

  {#each questions as { question, options }, index}
    <div class="question">{question}</div>
    {#each options as option}
      <div class="option {userAnswers[index] === option ? 'selected' : ''}" 
           on:click={() => userAnswers[index] = option}>
        {option}
      </div>
    {/each}
  {/each}

  <div class="input-container">
    <input type="text" bind:value={goal} placeholder="Введите вашу цель..."/>
    {#if buttonVisible}
      <button on:click={getGoals}>Получить цели</button>
    {/if}
  </div>

  <div class="goals">
    <h2>Ваши цели:</h2>
    <ul>
      {#each parsedData as [goal, subgoals]}
        <li>
          <strong>{goal}</strong>
          {#if subgoals.length > 0}
            <ul>
              {#each subgoals as subgoal}
                <li>{subgoal}</li>
              {/each}
            </ul>
          {/if}
        </li>
      {/each}
    </ul>
  </div>
</div>