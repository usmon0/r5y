from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def index(request):
    return render(request, "index.html")

def getStudents(request):
    rows = Stuednts.objects.all()
    
    my_list = []

    for row in rows:
        my_list.append({    'id':row.id,
                            'name':row.name,
                            'image':row.image   })
        
    return JsonResponse({"values":my_list})


