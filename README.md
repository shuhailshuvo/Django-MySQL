# Django

DIY-2: Simple website using django & MySQL

# Installation

Simply installing django
`pip3 install django==2.1.7`
mysql doen't work in 3.0.2 or I couldn't make it work

`django-admin startproject` followed by Project Name will create new Project with basic skeleton
`django-admin startproject DjangoWeb`
Basic skeleton comes with a `manage.py` and the project directory.
`manage.py` is Django's command-line utility for administrative tasks.
Project directory contains following files:

    __init__.py

        This is an empty file that instructs Python to treat this directory as a Python package.

    - wsgi.py

        Web Server Gateway Interface is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request. It’s commonly provided as an object named application in a Python module accessible to the server.

    - asgi.py

        Python standard for asynchronous web servers and applications. When you want to enable channels in production, you need to do three things: 1. Set up a channel backend, 2. Run worker servers, 3. Run interface servers. Routing all traffic through the interface server lets you have WebSockets and long-polling coexist in the same URL tree with no configuration

    - settings.py

        Contains the configuration for while application including but not limited to debug mode, IP whitelisting, installed app, middlewares, template, database, authentication, locale, timezone etc.

    - urls.py

        This is the routing table for the application. `path()` is imported from `django.urls` and registered in `urlpatterns` list.
        `path()` takes two parameters, 1. url/route and 2. target method to forward the request.
        `path('/', views.class.method)` simple route.
        `path('/<int:resourceId>', views.class.method)` route with variable.
        `re_path(r'^([0-9]+)/$', views.class.method)` route with regex match

Starting django server
`python DjangoWeb/manage.py runserver`

Creating application under this project
`python3 manage.py startapp user`

# Basic Configurations

Registering the User app into `INSTALLED_APPS`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user'
]
```

Adding mysql & mongodb configuration

install `pymysql`

`pip3 install pymysql`

Expose `pymysql` as `MYSQLDB` in `__init__.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'NAME': 'pydb',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```

To install mongo db,
Djongo needs to be install.
`pip install Djongo`

```
DATABASES = {
    'mongo': {
        'ENGINE': 'djongo',
        'USER': '',
        'NAME': 'pydb',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 27017,
    }
}
```

Database routing can be used to route specific request to a database.

# Routing

The `urlpatterns` list routes URLs to views.
Examples:
Function views

1. Add an import: `from app.views.users import userList`
2. Add a URL to urlpatterns: `path('/', userList, name='home')`

Class-based views

1. Add an import: `from other_app.views import Home`
2. Add a URL to urlpatterns: `path('', Home.as_view(), name='home')`

Including another URLconf

1. Import the include() function: `from django.urls import include, path`
2. Add a URL to urlpatterns: `path('blog/', include('blog.urls'))`

# View

Urls.py redirect each request to associated view function

```
def userList(request):
    return render(request, 'userList.html', {"users": Users.objects.all()}, content_type='text/html')
```

This view function will render the `userList.html` template with `uses` dictionary

# Template

```
<h1>Users</h1>
<table>
  {% for user in users %}
  <tr class="{% cycle 'row1' 'row2' %}">
    <td>{{user.name}}</td>
  </tr>
  {% endfor %}
</table>

```

For all templating functions, check this [link](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)

# Models

```
from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=66)

```

Models define the structure, relation & [Much More](https://docs.djangoproject.com/en/3.0/topics/db/models/)

# Forms

Django can handle HTML forms easily. Form `action` will redirect to url and request will have form data under `method`

```
def userLogin(request):
    login = request.POST
    # login['email']
    # login['password']
```

Form can be created with django forms

```
from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(label='Your name')
    email = forms.EmailField(label='Your Email')
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
```

To user this form:

```
signupForm = SignUpForm()
return render(request, 'signup.html', {'form': signupForm}, content_type='text/html')
```

To render the form in template

```
 <form action="/users/signup" method="post">
    {{ form }}
    <button type="submit" class="submit">Sign Up</button>
</form>
```

# Session

Django by default enable session by putting session middleware in `settings.py`
`'django.contrib.sessions.middleware.SessionMiddleware'`

And store session data in database by putting session in `INSTALLED_APPS`
`'django.contrib.sessions'`

Session can also be used with cache, cookie & file. Read [This](https://docs.djangoproject.com/en/3.0/topics/http/sessions/)
