from django.shortcuts import render,get_object_or_404
from .models import Item,OrderItem,Order
from django.shortcuts import render, redirect
from django.http import HttpResponse

#DataFlair #View Caching
from django.views.decorators.cache import cache_page
cache_page(200)
#definition of the view function

def item_list(request):
	context = {
	'item': Item.objects.all()
	}
	return render(request, 'home-page.html', context)

def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    html.set_cookie('core', 'Hello this is your Cookies', max_age = None)
    return html

def showcookie(request):
    show = request.COOKIES['core']
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)

def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>core<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')