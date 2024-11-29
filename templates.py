HTML_TEMPLATE = """
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Фотохостинг</title>
    <style>
        /* Основные стили */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            color: white;
            background: url('https://img1.akspic.ru/crops/0/6/5/3/7/173560/173560-dodzh_chellendzher-dodge-dodge_challenger_2021_goda-dodzh_demon-legkovyye_avtomobili-2560x1440.jpg') no-repeat center center fixed;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        /* Эффект размытия и затемнения */
        body::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(10px);
            z-index: -1;
        }

        /* Контейнер */
.container {
    text-align: center;
    padding: 30px;
    background: linear-gradient(135deg, rgba(20, 20, 60, 0.85), rgba(30, 30, 80, 0.85)); /* Темно-синий с градиентом */
    border-radius: 20px;
    box-shadow: 0 15px 50px rgba(0, 0, 0, 0.7);
    transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
}

.container:hover {
    transform: scale(1.05);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
    background: linear-gradient(135deg, rgba(20, 20, 60, 0.9), rgba(30, 30, 80, 0.9));
}

/* Заголовок */
h1 {
    margin-top: 0;
    font-size: 3.5em;
    color: #00c3ff; /* Яркий голубой для контраста */
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.8), 0 0 30px rgba(0, 195, 255, 0.8); /* Яркое свечение */
    animation: fadeInDown 1s ease, pulse 1.5s infinite alternate;
}

@keyframes fadeInDown {
    0% {
        opacity: 0;
        transform: translateY(-50px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulse {
    0% {
        transform: scale(1);
    }
    100% {
        transform: scale(1.05);
    }
}

/* Добавление плавных анимаций для текста */
.container p {
    font-size: 1.2em;
    color: #ccc;
    opacity: 0;
    animation: fadeIn 2s forwards 0.5s;
}

@keyframes fadeIn {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}

/* Эффект пульса для кнопок или ссылок */
.container a {
    text-decoration: none;
    font-size: 1.2em;
    color: #00c3ff;
    padding: 10px 20px;
    border: 2px solid #00c3ff;
    border-radius: 10px;
    margin-top: 20px;
    display: inline-block;
    transition: all 0.3s ease;
}

.container a:hover {
    background-color: #00c3ff;
    color: #fff;
    transform: scale(1.1);
}

/* Тень для контейнера */
.container {
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.6), 0 15px 40px rgba(0, 0, 0, 0.5);
}


        @keyframes fadeInDown {
            0% {
                opacity: 0;
                transform: translateY(-50px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Кнопка загрузки */
        .cta {
            display: inline-flex;
            padding: 12px 40px;
            font-size: 1.2em;
            color: white;
            background: linear-gradient(45deg, #6225e6, #fbc638);
            border: none;
            cursor: pointer;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            transition: all 0.4s ease;
            transform: skewX(-10deg);
            box-shadow: 8px 8px 0 black;
        }

        .cta:hover {
            box-shadow: 10px 10px 0 #fbc638;
            background: linear-gradient(45deg, #fbc638, #6225e6);
        }

        .span {
            transform: skewX(10deg);
        }

        /* Ссылка */
        a {
            color: #fbc638;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease, text-shadow 0.3s ease;
        }

        a:hover {
            color: #ffffff;
            text-shadow: 0 0 15px #fbc638;
        }

        /* Секция загрузки */
        .loading {
            display: none;
            justify-content: center;
            align-items: center;
            font-size: 1.5em;
            color: #fbc638;
        }

        .loading.active {
            display: flex;
        }

        .pl {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 14em;
            height: 14em;
        }

        .pl__dot {
            width: 1.5em;
            height: 1.5em;
            background-color: white;
            border-radius: 50%;
            animation: loading 1.5s linear infinite;
            margin: 0 0.2em;
        }

        @keyframes loading {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.5);
            }
        }

        /* Выпадающее меню */
        .dropdown-container {
            border: 2px solid #fbc638;
            border-radius: 8px;
            padding: 10px;
            margin-top: 20px;
            background-color: rgba(0, 0, 0, 0.8);
        }

        .dropdown-container select {
            background-color: #6225e6;
            color: white;
            border: none;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            text-align: center;
        }

        /* Мелкие эффекты */
        footer {
            margin-top: 20px;
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9em;
        }

        footer a {
            color: #fbc638;
        }

        footer a:hover {
            color: white;
            text-shadow: 0 0 10px #fbc638;
        }
    </style>
    <script>
        function showLoading() {
            document.getElementById('loading').classList.add('active');
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>Загрузите свое фото</h1>
        <form method="post" enctype="multipart/form-data" onsubmit="showLoading()">
            <input type="file" name="file" required>
            <button class="cta" type="submit">
                <span class="span">Загрузить</span>
            </button>
        </form>
        <div id="loading" class="loading">
            <div class="pl">
                <div class="pl__dot"></div>
                <div class="pl__dot"></div>
                <div class="pl__dot"></div>
            </div>
            <p>Загрузка...</p>
        </div>
        {% if url %}
        <h2>Файл успешно загружен!</h2>
        <p>Ссылка на фото:</p>
        <a href="{{ url }}" target="_blank">{{ url }}</a>
        <p>Имя файла: {{ url.split("/")[-1] }}</p>
        {% endif %}

        <div class="dropdown-container">
            <select onchange="window.location.href=this.value">
                <option value="#">Выберите действие</option>
                <option value="https://vk.com/your_bot">Перейти к боту ВКонтакте</option>
                <option value="https://vk.com/another_option">Дополнительная опция</option>
            </select>
        </div>
    </div>
    <footer>
        © 2024 Фотохостинг. Все права защищены. | <a href="#">Политика конфиденциальности</a>
    </footer>
</body>
</html>
<style>
    footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        background: rgba(0, 0, 0, 0.7);
        color: white;
        padding: 10px 0;
        font-size: 0.9em;
    }
</style>

"""
