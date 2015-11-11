from django import forms
from .models import Listings

class ListingsForm(forms.ModelForm):

    class Meta:
        model = Listings
        fields = ('title', 'price', 'condition', 'comments', 'title', 'isbn', 'edition', 'author', 'longitude', 'latitude', 'expirationdate',)