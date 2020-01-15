from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.models import Users
from .Forms import signup
import requests


def userList(request):
    if request.session['userId']:
        return render(request, 'userList.html', {"users": Users.objects.all()}, content_type='text/html')
    else:
        return welcome(request, 'Login to get access')


def userLogin(request):
    try:
        login = request.POST
        loggedInUser = Users.objects.get(
            email=login['email'], password=login['password'])

        request.session['userId'] = loggedInUser.id
        return HttpResponseRedirect("/users/list")
    except:
        return welcome(request, "Invalid Credentials")


def userSignup(request):
    try:
        if request.method == "POST":
            form = signup.SignUpForm(request.POST)
            if form.is_valid():
                newUser = Users(
                    name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
                newUser.save()
                form.clean()
                request.session['userId'] = newUser.id
                return HttpResponseRedirect("/users/list")
    except:
        return welcome(request, "Already Registered! Try Login")


def welcome(request,  error='', cookieName='', cookieVal='defaultBg'):
    if 'userId' in request.session:
        return userList(request)
    else:
        signupForm = signup.SignUpForm()
        options = {
            "error": error,
            'form': signupForm,
            "color": cookieVal
        }
        return render(request, 'welcome.html', options, content_type='text/html')


def userLogout(request):
    if "userId" in request.session:
        del request.session["userId"]
    return welcome(request)


def userDetails(request, id):
    # resp = requests.get('https://www.mocky.io/v2/5185415ba171ea3a00704eed'+str(id))
    # details = resp.json()
    return render(request, 'details.html', {"user": [id, "User Name", "Email", "phone"]}, content_type='text/html')
