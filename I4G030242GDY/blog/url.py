from django.urls import path
from .views import bblogview

urlpatterns = [
            path('', blogview.as_view(), name='home')
]