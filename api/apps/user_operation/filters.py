import django_filters
from .models import Reviews


class ReviewsFilter(django_filters.rest_framework.FilterSet):
    """
    Reviewsのfilter
    """
    star = django_filters.NumberFilter(field_name="star", lookup_expr='lte')

    class Meta:
        model = Reviews
        fields = ['star']
