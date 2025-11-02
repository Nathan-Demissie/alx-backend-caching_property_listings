from django.views.decorators.cache import cache_page
from django.shortcuts import render
from properties.models import Property

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/list.html', {'properties': properties})
