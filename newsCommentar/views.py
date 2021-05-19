from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Kommentar, User
from .forms import KommentarForm
# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    form = KommentarForm()
    # get all comments
    comments = Kommentar.objects.all().order_by('-timestamp')
    return render(request, 'news/index.html', {
        'form': form,
        'comments': comments
    })


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # check if password == confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, 'news/register.html', {
                'massage': 'Bitte gebe zwei mal das selbe Passwort ein'
            })
        # check if user exists
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, 'news/register.html', {
                'massage': 'Bitte nurtze einen anderen Usernamen'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'news/register.html')


def logout_view(request):
    logout(request)
    return render(request, 'news/register.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "news/login.html", {
                "message": "Falsches Passwort und/oder username."
            })
    else:
        return render(request, "news/login.html")


@csrf_exempt
def comment(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        data = json.loads(request.body)
        new_comment = Kommentar(post=data['text'], user=user)
        new_comment.save()
        return JsonResponse([new_comment.serialize()], safe=False)
