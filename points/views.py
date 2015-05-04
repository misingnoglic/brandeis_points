from django.shortcuts import render, HttpResponse
from points_request2 import *
import os
#import secrets
import json
# Create your views here.
brandeis_user = os.environ["arya_brandeis_username"]
brandeis_pass = os.environ["arya_brandeis_password"]

def get_meals(request):
    data = get_html(brandeis_user,brandeis_pass)
    d = {"points":data[0], "meals":data[1]}
    return HttpResponse(json.dumps(d), content_type="application/json")

def config(request):
    if request.method=='POST':
        pass
#