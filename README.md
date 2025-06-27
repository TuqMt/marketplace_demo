#  Flask Маркетплейс

Веб-приложение на Flask, позволяющее просматривать список товаров, покупать их и отслеживать историю покупок.

##  Функционал

- Просмотр списка товаров с изображениями
- Кнопка "Купить" с добавлением записи в историю
- Просмотр истории всех покупок
- Простой адаптивный интерфейс
- Использование PostgreSQL как базы данных

---

##  Запуск проекта

### 1. Установи зависимости:

```
pip install flask psycopg2
```

### 2. Подготовь базу данных PostgreSQL:
Создай БД testbase и таблицы:
```
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    price INTEGER,
    category TEXT,
    image_url TEXT
);

CREATE TABLE buys (
    id SERIAL PRIMARY KEY,
    date DATE,
    name TEXT,
    price INTEGER
);
```

### 3. Добавь товары (пример запроса):
```
INSERT INTO items (name, description, price, category, image_url) VALUES
('Яблоко', 'Свежее красное яблоко', 120, 'Фрукты', 'https://loremflickr.com/320/240/apple'),
('Банан', 'Спелый банан из Эквадора', 180, 'Фрукты', 'https://loremflickr.com/320/240/banana'),
-- Добавь свои товары по аналогии
;
```

4. Запусти сервер:
```
  python app.py
```
Открой в браузере:

  http://127.0.0.1:5000

### Публикация через Ngrok (по желанию)
Если хочешь поделиться приложением онлайн:

```
ngrok config add-authtoken <твой_токен>
ngrok http 5000
```
#### Структура проекта


├── app.py                  # Flask-приложение 

├── templates/  

│   ├── home.html           # Главная страница

│   ├── index.html          # Страница товаров

│   └── profile.html        # История покупок

└── README.md               # Этот файл

