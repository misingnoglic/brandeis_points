from django.shortcuts import render, HttpResponse
from points_request2 import get_html
import os
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_meals(request):
    if request.method == 'POST':
            brandeis_user = request.POST["username"].lower()
            brandeis_pass = request.POST["password"]
    
            data = get_html(brandeis_user,brandeis_pass)
    d = {"points":data[0], "meals":data[1]}
    return HttpResponse(json.dumps(d), content_type="application/json")