from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class CustomPageNumber(pagination.PageNumberPagination):
    page_size = 9

    def get_paginated_response(self, data):
        return Response({
            'current': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class CustomUserProdPageNumber(pagination.PageNumberPagination):
    page_size = 4

    def get_paginated_response(self, data):
        return Response({
            'current': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })