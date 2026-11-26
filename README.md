# 🎮 Game DB

A simple web application for displaying a collection of video games. The project uses Django REST Framework as a backend API and JavaScript for displaying data on the frontend.

## 📸 Preview

The website displays games in cards with their images, descriptions, categories, and prices.

## ✨ Features

- Display a list of video games.
- Load game information from a Django REST Framework API.
- Display game images and descriptions.
- Show game categories and prices.
- Dark theme interface.
- Switch between available website themes.

## 🛠️ Technologies

**Backend:**
- Python
- Django
- Django REST Framework
- PostgreSQL

**Frontend:**
- HTML5
- CSS3
- JavaScript
- Fetch API

## 📂 Project Structure

```text
Game-DB/
│
├── game_db/
│   ├── game_db/
│   ├── games/
│   └── manage.py
│
└── game_db_frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/amirbek302/game-db.git
```

### 2. Open the backend directory

```bash
cd game_db
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start Django server

```bash
python manage.py runserver
```

### 7. Open the frontend

Open `game_db_frontend/index.html` using your local development server.

## 🔗 API Endpoint

The frontend retrieves game information from:

```text
http://127.0.0.1:8000/api/v1/game_db/
```

The API provides information about:

- Game name
- Description
- Category
- Price
- Creation date
- Game thumbnail

## 🎨 Theme

The website includes a dark interface and a theme switcher that allows users to change the appearance of the website.

## 📌 Project Status

The project is currently under development.

## 👨‍💻 Author

Developed as a personal learning project to practice Django REST Framework, JavaScript, API integration, and frontend development.
