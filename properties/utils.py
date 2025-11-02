import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from properties.models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    """Retrieve all properties from cache or database."""
    properties = cache.get('all_properties')

    if properties is None:
        try:
            properties = list(Property.objects.all().values(
                'title', 'description', 'price', 'location', 'created_at'
            ))
            cache.set('all_properties', properties, timeout=3600)  # Cache for 1 hour
            logger.info("Cached all_properties queryset in Redis.")
        except Exception as e:
            logger.error(f"Error fetching properties: {e}")
            properties = []

    return properties


def get_redis_cache_metrics():
    """Analyze Redis cache hit/miss metrics and return summary."""
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info()

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0

        metrics = {
            "hits": hits,
            "misses": misses,
            "hit_ratio": round(hit_ratio, 4)
        }

        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics

    except Exception as e:
        logger.error(f"Failed to retrieve Redis cache metrics: {e}")
        return {
            "hits": 0,
            "misses": 0,
            "hit_ratio": 0
        }
