from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import *

# deprecated
from django.http import HttpResponse
from django.template.loader import get_template

BASE_MODAL_LINKS_DICT = {'text' : "INICIAR SESSION", 'url' : "login.html" }
BASE_MODAL_LINKS_LIST = [ BASE_MODAL_LINKS_DICT ]

BASE = {
        'BASE_TITLE' : "cuceipark!",
        'BASE_MAIN_TITLE' : "ENCUENTRA SIEMPRE UN LUGAR",
        'BASE_MODAL_LINKS_LIST' : BASE_MODAL_LINKS_LIST,
        'BASE_MODAL_TITLE' : "cuceipark!",
        'BASE_MODAL_CLOSE' : "menu principal",
        'BASE_FOOTER_TITLE' : "cuceipark!",
        'BASE_FOOTER_SUBTITLE' : "",
        'BASE_FOOTER_MEDIUM' : "REGRESAR ARRIBA",
        'BASE_FOOTER_LAST' : "cucei open source community"
}

def index(request):
	t = get_template('index.html').render(BASE)
	return HttpResponse(t)

def index(request):
    t = get_template('index.html').render(BASE)
    return HttpResponse(t)

def register_client(request):
    t = get_template('register_client.html').render()
    return HttpResponse(t)

def register_investment(request):
    t = get_template('register_investment.html').render()
    return HttpResponse(t)

def investment_panel(request):
    t = get_template('investment_panel.html').render()
    return HttpResponse(t)

