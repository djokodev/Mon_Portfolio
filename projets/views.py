from django.shortcuts import render, redirect

from projets.models import Projet


def home(request):
    projet = Projet.objects.all()  #on met le model projet dans une variable 'projet'
    context = {"projet":projet}
    return render(request,"home.html",context)
