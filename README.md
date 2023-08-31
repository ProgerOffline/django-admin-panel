# django-web-panel 😺

## Table of Contents 📚

- [Description](#description-)
- [Project Structure](#project-structure-)
- [Key Features](#key-features-)
  - [Design](#design)
  - [Functionality](#functionality)
  - [Technologies](#technologies)
- [Installation Guide](#installation-guide)
- [License](#license)
- [Support the Author](#support-the-author)
- [Demo Videos](#demo-videos)

## Description 📜
**django-web-panel** is a Git repository that contains a versatile template for quickly creating a web admin panel with modern design and comprehensive functionality. This template offers a convenient solution for developers aiming to build functional administrative panels for various purposes, such as online stores, data management systems, analytical platforms, and more.

## Project Structure

```
.
├── .env-dist
├── postgres-utils.py
├── README.md
├── requirements.txt
└── src
    └── web
        ├── accounts
        ├── manage.py
        ├── panel
        ├── static
        ├── templates
        └── web
```

## Key Features 🚀

### Design 🎨
- Modern and responsive design, adaptable to different devices. 🌐
- Minimalistic and intuitively designed interface for easy navigation. 🧭

### Functionality ⚙️
- User registration and account management with support for different roles and access rights. 👥
- User authentication and authorization for data security. 🔐
- Flexible database management system for storing and processing information. 🗄️

### Technologies 💻
- Built using popular web technologies such as HTML, CSS, and JavaScript. 🌐
- Web framework Django for faster development and feature extension. 🐍
- Integration capability with database PostgreSQL. 📊

## Database Management 🗃️

The repository includes a helpful file named `postgres-utils.py` which provides commands for managing the database. Here are the available commands:

- `db-update-access`: Grants privileges to the database for the environment user.
- `db-remove`: Removes the environment database.
- `db-create`: Creates the environment database.
- `db-recreate`: Recreates the environment database.

## Demo Videos 📹

![Desktop version](https://github.com/ProgerOffline/django-admin-panel-template/assets/70508510/67b89466-4764-4d66-8192-b1def6ad8078)

![Mobile version](https://github.com/ProgerOffline/django-admin-panel-template/assets/70508510/cd2919a0-585c-4ed5-b3a3-0c903077f4a9)


## Installation Guide 🛠️

To set up the project, follow these steps:

1. Clone the repository:
```Shell
git clone https://github.com/ProgerOffline/django-web-panel
cd django-web-panel
```

2. Edit the `.env-dist` file with the following content:
```python3
DATABASE_NAME=
DATABASE_USERNAME=
DATABASE_PASSWORD=
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```

Rename the file to `.env`.

3. Create a Python 3 virtual environment:
```Shell
python3 -m venv venv
source venv/bin/activate
```

4. Install the required packages from the `requirements.txt` file:
```Shell
pip install -r requirements.txt
```

5. Navigate to the `src/web/` directory:
```Shell
cd src/web/
```

6. Apply migrations for the Django database:
```Shell
python3 manage.py makemigrations
```

7. Apply the migrations to the Django database:
```Shell
python3 manage.py migrate
```

8. Start the Django project:
```Shell
python3 manage.py runserver
```
Now the project is set up and running. You can access the admin panel and start building your application.

## Support the Author ❤️

If you find this project helpful and would like to support the author, you can consider contributing to the project, giving it a star on GitHub, or providing a donation.
