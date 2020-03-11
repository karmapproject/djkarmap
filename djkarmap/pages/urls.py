from django.urls import path
from .views import JobOrderListView


urlpatterns = [
    path('', JobOrderListView.as_view(), name='home'),
]