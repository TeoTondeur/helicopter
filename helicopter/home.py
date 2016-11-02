from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import *
from plans.models import Profil

def index(request):
    if request.user.is_authenticated():
        profil=Profil.objects.filter(user=request.user.pk)[0]
        if profil.statut==2: #professeur
            ### on affiche la liste des profs, des élèves inscrits,
            ### et des élèves visiteurs
            pProf=Profil.objects.filter(statut=2).order_by("user__last_name","user__first_name")
            pEleve=Profil.objects.filter(statut=1).order_by("user__last_name","user__first_name")
            pVisiteur=Profil.objects.filter(statut=0).order_by("user__last_name","user__first_name")
            return render(
                request,
                "home_prof.html",
                {
                    "profil"    : profil.verbose_statut(),
                    "profs"     : [p.user for p in pProf],
                    "eleves"    : [p.user for p in pEleve],
                    "visiteurs" : [p.user for p in pVisiteur],
                }
            )
        else: # pas prof
            return render(
                request,
                "home.html",
                {
                    "profil": profil.verbose_statut()
                }
            )
    else:
        return HttpResponseRedirect("/login/")

