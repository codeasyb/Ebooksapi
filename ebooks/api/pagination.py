from rest_framework.pagination import PageNumberPagination

# create custom class for pagination
class SmallSetPagination(PageNumberPagination):
    """
    Pagination is not efficient and will throw errors for 
    unordered list in the database queryset
    """
    page_size = 3