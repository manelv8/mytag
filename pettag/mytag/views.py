from django.shortcuts import render , render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import FormUser

# Create your views here.
def index(request):
	return render_to_response("index.html")

def registrar(request):
	
	if request.method == 'POST':
	    form = FormUser(request.POST)

	    if form.is_valid():
	    	form.save()
	    	return HttpResponseRedirect("/login/")	
	    else:
	    	return render(request, "registrar.html", { "form": form })

	return render(request, "registrar.html", {"form": FormUser() })

def login(request):
    return render(request, "login.html", {})


