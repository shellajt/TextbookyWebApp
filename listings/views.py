from django.shortcuts import render
from .models import Listings
from .forms import ListingsForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def listing_list(request):
        listings = Listings.objects.order_by('expirationdate')
        return render(request, 'listings/listing_list.html', {'listings': listings})
		
def newlisting(request):
    if request.method == "POST":
        form = ListingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listings/')
    else:
        form = ListingsForm()
    return render(request, 'newlisting/newlisting.html', {'form':form})		
