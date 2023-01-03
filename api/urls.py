from vendor.views import *
from django.urls import path

urlpatterns = [
    path('vendors/', VendorView.as_view()),
    path('vendors/<pk>', VendorDetailsView.as_view()),
]
