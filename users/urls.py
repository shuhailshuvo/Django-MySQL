from django.contrib import admin
from django.urls import path, include
from users.views.users import userList, userLogin, userSignup, welcome, userLogout, userDetails

urlpatterns = [
    path('/', welcome),
    path('/login', userLogin),
    path('/signup', userSignup),
    path('/logout', userLogout),
    path('/list', userList, name='users'),
    path('/details/<id>', userDetails, name='Details'),
    path('/<cookieName>/<cookieVal>', welcome, name='Welcome')
]
