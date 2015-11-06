from django.shortcuts import render
from .models import Listings, Users
from .forms import ListingsForm
from django.shortcuts import redirect
from django.utils import timezone
from decimal import Decimal

# Create your views here.
def listing_list(request):
        listings = Listings.objects.order_by('expirationdate')
        return render(request, 'listings/listing_list.html', {'listings': listings})
		
def newlisting(request):
    if request.method == "POST":
        form = ListingsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.postdate = timezone.now()
            form.userid = Users.objects.get(pk=2)
            form.negotiable = True
            form.save()
            return redirect('/listings/')
    else:
        form = ListingsForm()
    return render(request, 'newlisting/newlisting.html', {'form':form})		

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip