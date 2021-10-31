from django.http import JsonResponse
from django.shortcuts import render
from .models import MyModel
from django import views
# Create your views here
from django.db import transaction

from parallelproject import tasks
import requests
import time
class MyView(views.View):
    def get(self, request):
        q1 = request.GET.get("q1")
        if q1:
            print("I am inside q1")
            mm = MyModel.objects.create(param_name="q1",value=str(q1))
            print("I have inserted into database")
            res = tasks.process.apply_async([q1], countdown=10)
            return JsonResponse({"response":"request string for q1 is {}".format(q1)})

class TestDriver(views.View):
    def get(self,request):
        
        return render(request,"test.html")
    def post(self,request):
        q1 = request.POST.get("q1")
        url = request.build_absolute_uri("test")
        params = {"q1": str(q1)}
        r = requests.get(url=url, params=params)
        return render(request, "test.html",{"q1":str(r.json())})
