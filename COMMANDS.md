# quickstart

```
mkdir tutorial
cd tutorial
pip install django -U
pip install djangorestframework -U 
django-admin.py startproject tutorial
cd tutorial
django-admin.py startapp quickstart
cd ..
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin  # password123
vim tutorial/quickstart/serializers.py
vim tutorial/quickstart/views.py
vim tutorial/urls.py
vim tutorial/settings.py
python manage.py runserver
http http://127.0.0.1:8000/users/
```

