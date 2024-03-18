# clients/urls.py
from django.urls import path
from .views import CompanyViewSet

app_name = 'clients'

urlpatterns = [
    path('', CompanyViewSet.as_view({'get': 'list', 'post': 'create'}), name='company-list'),
    # Add more URLs specific to the clients app if needed
]
