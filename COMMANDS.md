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
http http://127.0.0.1:8000/quickstart/users/
```

# 1

```
pip install pygments  # We'll be using this for the code highlighting
python manage.py startapp snippets
vim tutorial/settings.py
vim sinppets/models.py
python manage.py makemigrations snippets
python manage.py migrate
vim snippets/serializers.py
mkdir -p snippets/management/commands
vim snippets/management/commands/snippets_seed.py
vim snippets/serializers.py
vim snippets/management/commands/snippets_seed.py
vim snippets/views.py
vim snippets/urls.py
vim tutorial/urls.py
http http://127.0.0.1:8000/snippets/
http http://127.0.0.1:8000/snippets/21/
```

# 2

```
vim snippets/views.py
vim snippets/urls.py
http http://127.0.0.1:8000/snippets/
http http://127.0.0.1:8000/snippets/ Accept:application/json
http http://127.0.0.1:8000/snippets/ Accept:text/html
http http://127.0.0.1:8000/snippets.json
http http://127.0.0.1:8000/snippets.api
http --form POST http://127.0.0.1:8000/snippets/ code="print 123"
http --json POST http://127.0.0.1:8000/snippets/ code="print 456"
```

# 3

```
vim snippets/views.py
vim snippets/urls.py
vim snippets/views.py
```
