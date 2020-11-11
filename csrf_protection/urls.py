from django.urls import path
from csrf_protection import views

app_name = 'csrf_protection'

urlpatterns = [
    path("", views.csrf_index, name='csrf_index'),
    path("without_protection/", views.without_protection, name='without_protection'),
    path("with_standard_protection/", views.with_standard_protection, name='with_standard_protection'),
    ]
