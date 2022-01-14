## Language used: 
* Python v3.10.1

<br/>

## Framework used: 
* Django v4.0.1,
* Django Rest Framework v3.13.1

<br/>

## Database used: 
* SQLite 


<br/>

## Step 1(Download):
* Download [python 3.10.1](https://www.python.org/downloads/)

<br/>

## Step 2(Install):
* Run 'python-3.10.1-amd64.exe' as administrator.
* Don't forget to check add to path(windows)

<br/>

## Step 3(Repository):
* Git Clone 'https://github.com/MrNewaz/Coding-Assignment.git'
* Or Download code from the repository.

<br/>

## Step 4(Virtual Environment):
* Open the folder in an IDE(e.g. VSCode) and Run 'pipenv shell' in the terminal to activate virtual environment.

<br/>

## Step 5(Install Dependencies):
* Run 'pipenv install' in the terminal to install all dependencies.

<br/>



## Step 6(Migrations):
* Run 'python manage.py makemigrations'.
* Run 'python manage.py migrate'. 

<br/>

## Step 7(Adding Superuser):
* Run 'python manage.py createsuperuser' in the terminal and create a superuser to access admin pannel by adding username, email(optional) and password.

<br/>

## Step 8(Run App):
* Run 'python manage.py runserver' to start the server.

<br/>

## Step 9(Test App):
* Run 'python manage.py test' for testing APIs.

<br/>

## Done!:
* That's all. Thank you. Have a nice day.


<br/>

# Urls(After Step 8):

## [Admin Pannel](http://127.0.0.1:8000/admin/)
## [Parent](http://127.0.0.1:8000/user/parent/)
## [Child](http://127.0.0.1:8000/user/child/)

# Tree:

|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- core
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-310.pyc
|   |   |-- settings.cpython-310.pyc
|   |   |-- urls.cpython-310.pyc
|   |   |-- views.cpython-310.pyc
|   |   `-- wsgi.cpython-310.pyc
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- db.sqlite3
|-- manage.py
`-- user
    |-- __init__.py
    |-- __pycache__
    |   |-- __init__.cpython-310.pyc
    |   |-- admin.cpython-310.pyc
    |   |-- apps.cpython-310.pyc
    |   |-- models.cpython-310.pyc
    |   |-- serializers.cpython-310.pyc
    |   |-- tests.cpython-310.pyc
    |   |-- urls.cpython-310.pyc
    |   `-- views.cpython-310.pyc
    |-- admin.py
    |-- apps.py
    |-- migrations
    |   |-- 0001_initial.py
    |   |-- 0002_alter_child_options.py
    |   |-- 0003_alter_child_parent.py
    |   |-- __init__.py
    |   `-- __pycache__
    |       |-- 0001_initial.cpython-310.pyc
    |       |-- 0002_alter_child_options.cpython-310.pyc
    |       |-- 0003_alter_child_parent.cpython-310.pyc
    |       `-- __init__.cpython-310.pyc
    |-- models.py
    |-- serializers.py
    |-- tests.py
    |-- urls.py
    `-- views.py

6 directories, 39 files