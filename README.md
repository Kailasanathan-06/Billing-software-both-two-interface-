File structure:
grocery_shop/
│
├── manage.py
│
├── grocery_shop/
│   ├── settings.py
│   └── urls.py
│
└── shop/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
        ├── shopkeeper.html
        └── customer.html


HOW TO RUN (FINAL)
Step 1 — Install
pip install django mysqlclient

Step 2 — Create DB in Workbench
CREATE DATABASE grocery_db;

Step 3 — Migrate
python manage.py makemigrations
python manage.py migrate

Step 4 — Run
python manage.py runserver

Step 5 — Open in browser

Shopkeeper → http://127.0.0.1:8000/shopkeeper/

Customer → http://127.0.0.1:8000/customer/
