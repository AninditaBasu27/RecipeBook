

# RecipeBook 🍳

A web-based recipe management system built with Python and Django. This application allows users to create, view, and manage their favorite recipes in a clean and organized interface.

## 🚀 Features

  * **User Authentication:** Secure signup and login system.
  * **Recipe Management:** Create, Read, Update, and Delete (CRUD) operations for recipes.
  * **Image Uploads:** Support for adding photos to recipes.
  * **Search Functionality:** Quickly find recipes by name or ingredients.
  * **Responsive Design:** Optimized for both desktop and mobile viewing.

## 🛠️ Tech Stack

  * **Backend:** Python, Django
  * **Database:** SQLite (default) / PostgreSQL
  * **Frontend:** HTML5, CSS3, Bootstrap
  * **Environment Management:** Python Virtual Environment (`venv`)

## ⚙️ Installation & Setup

Follow these steps to get the project running locally:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/AninditaBasu27/RecipeBook.git
    cd RecipeBook
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    *(Ensure you have a requirements.txt file; if not, install django and pillow)*

    ```bash
    pip install django pillow
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (to access the admin panel):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the server:**

    ```bash
    python manage.py runserver
    ```

    Access the app at `http://127.0.0.1:8000/`.

## 📁 Project Structure

```text
RecipeBook/
├── RecipeBook/        # Project settings
├── accounts/          # User authentication app
├── media/             # Uploaded recipe images
├── static/            # CSS, JS, and images
├── templates/         # HTML files
├── manage.py          # Django command-line utility
└── db.sqlite3         # Database
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\! Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/AninditaBasu27/RecipeBook/issues).

## 📄 License

This project is licensed under the MIT License.

-----
