from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('avocado/', views.avocado_predict),
]

urlpatterns = format_suffix_patterns(urlpatterns)
