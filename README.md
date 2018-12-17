# Django learning project

The project is for Django framework learning.
Setup:
1. install python (https://www.python.org/)
2. install django (https://docs.djangoproject.com/en/1.11/topics/install/)
3. create virtual env (by default: name should be ``django_learning_env`` in root directory)
4. for develop env use command: ``pip install -r requirements/develop.txt`` (for production need to use ``production.txt`` file). Pip must be from virtual environment.

---

**Install project**:

Use standard django app commands to manage the application.

``python manage.py migrate``: application runs all db migrations defined in project. By default data base is sqlite.

``python manage.py runserver 8080``: application runs server on 8080 port.

To use specific configurations(profiles) need to add CLI param ``--settings=``
 
(For example for using postgres db: ``--settings=django_learning.settings.local_pg``)

----

# Frontend for developer

1. install node, npm
2. install angular cli - npm install @angular/cli
3. switch directory to "frontend"
4. launch "npm -i" command
for run use ng serve command
