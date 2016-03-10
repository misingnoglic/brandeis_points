from django.shortcuts import render, HttpResponse
from points_request2 import get_html
import os
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_meals(request):
    if request.method == 'POST':
        try:
            brandeis_user = request.POST["username"].lower()
            brandeis_pass = request.POST["password"]
        except KeyError:
            d = {"success":False, "error":"POST Request data not complete"}
        try:
            data = get_html(brandeis_user,brandeis_pass)
            d = {"success":True,"points":data[0], "meals":data[1]}
        except ConnectionError: # Bad Login
            d = {"success":False, "error":"Incorrect Credentials"}
        
    else:
        d = {"success":False, "error":"Not Valid POST REQUEST"}
    return HttpResponse(json.dumps(d), content_type="application/json")