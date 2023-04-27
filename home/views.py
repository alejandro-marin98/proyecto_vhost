from django.shortcuts import render
from django.http import HttpResponse
from solicitudes import views as sol
from gestionLibros.views import getAllBooks
from login.models import User
from gestionLibros.models import Libros
def home(request):    
    return render(request, 'home.html')
