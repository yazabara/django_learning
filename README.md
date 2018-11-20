# Django learning project

The project is for Django framework learning.
Setup:
1. install python (https://www.python.org/)
2. install django (https://docs.djangoproject.com/en/1.11/topics/install/)

---

**Install project**:

Use standard django app commands to manage the application.

``python manage.py migrate``: application runs all db migrations defined in project. By default data base is sqlite.

``python manage.py runserver 8080``: application runs server on 8080 port.

To use specific configurations(profiles) need to add CLI param ``--settings=``
 
(For example for using postgres db: ``--settings=django_learning.settings.local_pg``)

----


