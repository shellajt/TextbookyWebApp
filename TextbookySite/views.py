from django.shortcuts import render, get_object_or_404
from .models import Listings

# Create your views here.
def home(request):
        return render(request, 'home/home.html', {})
		
def listing_detail(request, pk):
    listing = get_object_or_404(Listings, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})