from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render

# Create your views here.
def view_sample(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def view_http_response_forbidden(request):
    html_data = {"data":"fobidden"}
    html = "it is {{data}}"
    return HttpResponseForbidden(html)

def view_render(request):
    html_data = {"data":"forbidden"}
    return render(request, "http_response/html_with_css.html",html_data)
