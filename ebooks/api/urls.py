from django.urls import path
from ebooks.api.views import (EbookListCreateAPIView, EbookDetailAPIView, 
                              ReviewCreateAPIView, ReviewDetailAPIView)

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="ebook-list"),
    path("ebooks/<int:pk>", EbookDetailAPIView.as_view(), name="ebook-detail"),
    path("ebooks/<int:ebook_pk>/review", ReviewCreateAPIView.as_view(), name="ebook-review"),
    path("reviews/<int:pk>/", ReviewDetailAPIView.as_view(), name="review-detail"),
]
 
# https://www.django-rest-framework.org/api-guide/permissions/
# 405 ERROR
# The 405 Method Not Allowed error shouldn’t be confused with the 404 Not Found error. 
# A 404 tells you that the requested URL couldn’t be found or that it was entered incorrectly. 
# A 405 error message, on the other hand, confirms that the requested page does exist 
# (and the URL was input correctly), but an unacceptable HTTP method was used to make 
# the initial request.

# Here are just a few of the many different variations you might run across:

# 405 Not Allowed
# Method Not Allowed
# HTTP 405 Error
# HTTP Error 405 – Method Not Allowed
# HTTP 405 Method Not Allowed