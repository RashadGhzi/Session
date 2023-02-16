from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def setcookies(request):
    request.session['name'] = 'Sonam'
    request.session['fname'] = 'Kashyeap'
    request.session['lname'] = 'Rony'
    request.session['mname'] = 'Talukdar'
    return HttpResponse('Cookies set')


def getcookies(request):
    # cookie = request.session.get('name', default='There is no cookie')
    return render(request, 'student/getcookie.html')


def delcookies(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponse('cookies deleted.....')
