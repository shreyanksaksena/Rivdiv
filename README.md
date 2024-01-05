Setting Up Django Project
# Django app directory is invoices
Install Django and DRF:
1. pip install django djangorestframework
2. Create a new Django project:
   django-admin startproject myproject
3. cd myproject
   python manage.py startapp invoices
4. Making migrations:
   python manage.py makemigrations invoices
   python manage.py migrate
5. Running the server:
   python manage.py runserver

