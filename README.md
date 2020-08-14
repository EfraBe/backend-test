# backend-test
Test required for backend.

### Requirements
* Install Python 3.
* Install Django ```python -m pip install django```
* Install Djando Rest Framework ```python -m pip install djangorestframework```
* Run migrations: Into project folder run ```python manage.py makemigrations```
* Apply changes with ```python manage.py migrate```
* Run the aplicacion with ```python manage.py runserver```

### Endpoints
* */pageuser* To list, create, update and delete users.
* */course* To list, create, update and delete courses.
* */lesson* To list, create, update and delete lessons.
* */questions* To list, create, update and delete questions.
* */login*