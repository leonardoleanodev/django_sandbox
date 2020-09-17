from django.http import HttpResponse
from django.shortcuts import render
from forms_examples.forms import FormCharfield

# Create your views here.
def view_sample(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def form_charfield_render(request):
    import pdb; pdb.set_trace()
    form_charfield = FormCharfield(request.POST)
    html_data={'form':form_charfield}
    return render(request, 'forms_examples/form_charfield_render.html', html_data)