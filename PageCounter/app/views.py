from django.shortcuts import render, HttpResponse

# Create your views here.


def page_counter(request):
    pageCount = request.session.get('count', 0)
    count = pageCount + 1
    request.session['count'] = count
    return render(request, 'app/home.html', {'count': count})


def session_del(request):
    del request.session['count']
    request.session.flush()
    request.session.clear_expired()
    return HttpResponse('Session has deleted...')
