from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('login/',views.login)

]