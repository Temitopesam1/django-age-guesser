from django.urls import path
from . import views

urlpatterns = [
    path('human-age/', views.human_age_api, name='human-age-api'),
]
