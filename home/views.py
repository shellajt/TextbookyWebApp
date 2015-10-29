from django.shortcuts import render
from .forms import UserForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
        return render(request, 'home/home.html', {})
		
def newuser(request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/home/')
        else:
            form = UserForm()
        return render(request, 'home/newuser.html', {'form' : form})