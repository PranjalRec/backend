from django.urls import path
from . import views

urlpatterns = [
    path('ashva/',views.say_ashva),
    path('ashva_page',views.say_ashva_page)
]