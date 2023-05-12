from django.shortcuts import HttpResponse
from datetime import date


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date_view(request):
    current_date = date.today()
    if request.method == 'GET':
        return HttpResponse(current_date)


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
