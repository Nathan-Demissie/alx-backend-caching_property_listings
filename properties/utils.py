from django.core.cache import cache
from properties.models import Property

def get_all_properties():
    # Try to get cached queryset
    properties = cache.get('all_properties')
    
    if properties is None:
        # Cache miss: fetch from DB and store in Redis
        properties = list(Property.objects.all().values(
            'title', 'description', 'price', 'location', 'created_at'
        ))
        cache.set('all_properties', properties, timeout=3600)  # Cache for 1 hour
    
    return properties
