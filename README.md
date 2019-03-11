#Django learning project

The project is for Django framework learning.

Trello: https://trello.com/b/Cx65xYwu/django-learning-github

## Setup backend:
1. install python (https://www.python.org/)
2. install django (https://docs.djangoproject.com/en/1.11/topics/install/)
3. create virtual env (by default: name should be ``django_learning_env`` in root directory)
4. for develop env use command: ``pip install -r requirements/develop.txt`` (for production need to use ``production.txt`` file). Pip must be from virtual environment.

## Setup frontend 
1. install node, npm
2. install angular cli - npm install @angular/cli
3. switch directory to "frontend"
4. launch "npm i" command
---

## Run project:

You may run project in 2 ways:

**Running project via docker:**

```docker-compose build```

```docker-compose up```

***deprecated docker way:***

Switch to directory ``/docker`` and run command ``build-images-and-launch-containers.bat up``
By default application is available at http://localhost:4200/

----
**OR**

----

**Running project without docker**

######Backend

Use standard django app commands to manage the application.

``python manage.py migrate``: application runs all db migrations defined in project. By default data base is PostgreSQL.

``python manage.py runserver 8080``: application runs server on 8080 port.

To use localhost:8080/admin page superuser must to be created. 
To create super user run next command ``python manage.py createsuperuser --username=joe --email=joe@example.com`` - where username - new login, after that you will be prompted create new password

To use specific configurations(profiles) need to add CLI param ``--settings=``
 
(For example for using postgres db: ``--settings=django_learning.settings.local_pg``)

######Frontend

For run use ``ng serve`` command.
