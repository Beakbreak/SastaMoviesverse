from rest_framework.pagination import PageNumberPagination


class CustomNumberPagination(PageNumberPagination):
    page_size = 15

class SuggestionsPagination(PageNumberPagination):
    page_size = 10