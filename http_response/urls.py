from django.urls import path
from http_response import views

app_name = 'http_response'

urlpatterns = [
    path("sample", views.view_sample, name='http_reponse_sample'),
    path("forbidden", views.view_http_response_forbidden, name='http_response_forbidden'),
    path("render_html", views.view_render,name='render')
    ]
