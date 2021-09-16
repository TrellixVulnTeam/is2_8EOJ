from django.shortcuts import render

# Create your views here.
from Sprints.models import Sprint


def nuevoSprint(datosSprint):
    newSprint = Sprint(sprintNumber=datosSprint["sprintNumber"], fecha_inicio=datosSprint["fecha_inicio"],fecha_fin=datosSprint["fecha_fin"])
    newSprint.save()
    if datosSprint["historias"]:
        for historia in datosSprint["historias"]:
            print(historia)
            newSprint.historias.add(historia)

