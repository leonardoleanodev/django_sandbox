from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render

# TODO: add an index page with all links to every tipe django example

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
