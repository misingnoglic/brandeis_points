from django.shortcuts import render, HttpResponse
from points_request2 import *
import secrets
import json
# Create your views here.

def get_meals(request):
    data = get_html(secrets.brandeis_user,secrets.brandeis_pass)
    d = {"points":data[0], "meals":data[1]}
    return HttpResponse(json.dumps(d), content_type="application/json")

def config(request):
    if request.method=='POST':
        pass
