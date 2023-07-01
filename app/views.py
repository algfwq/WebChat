from django.shortcuts import render
from django.http import FileResponse
import os
# Create your views here.

def logo_down(request):
    file = open(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/logo/logo.ico', 'rb')
    response = FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="logo.ico"'
    return response

def login(request):
    return render(request, 'login.html')
