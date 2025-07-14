# Django-Server-Task

In this task I used Django Framework with Python instead of XAMPP with PHP, external Postgresql instead of MySql. 
I made this on a local server and database. 
I also added a condition to not accept any negative number in Age field.

This project is a simple Django web app that allows users to:
- Submit name and age through a form.
- Store data in a PostgreSQL external database.
- Display all records in a table.
- Toggle a boolean status (0/1) for each record using AJAX.
- Reflect the change immediately without page reload.

---

## Features
- Uses Django ORM connected to an external PostgreSQL DB.
- Styled with basic HTML + CSS (no Bootstrap).
- Real-time toggle functionality using JavaScript + fetch.
- Clean separation between logic (views), data (models), and presentation (templates).

## Setup Instructions
1. Download python "make sure to Add python to PATH"
2. Install Django using "pip install Django" in CMD 
3. Install Postgresql and create database name users (you can use my backup file) 
4. Install Mysite folder and open it using Visual Stuido Code.
5. You need to install psycopg2-binary.
6. You need to modify settings.py using your own information of your Database here: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'your_host',  # e.g. localhost or remote IP
        'PORT': '5432',
    }
}

7. Run migrations, in your terminal type: python manage.py migrate
8. Finally you can start the server, in your terminal type: python manage.py runserver

## Final Result DB + Webpage 
<img width="1907" height="968" alt="DBwithWebpageFinal" src="https://github.com/user-attachments/assets/e807ea21-5b8b-4660-8011-af56d5783a47" />
