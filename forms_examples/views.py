from django.http import HttpResponse
from django.shortcuts import render
from forms_examples.forms import (FormCharField, FormChoiceFieldSelect,
                                  FormChoiceFlexible, FormChoiceCascade)

# TODO: add an index page with all links to every tipe django example

# Create your views here.
def view_sample(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def form_charfield_render(request):
    if request.method == 'POST':
        form_charfield = FormCharField(request.POST)
    else:
        form_charfield = FormCharField()

    html_data={'form_charfield':form_charfield}
    return render(request, 'forms_examples/form_charfield_render.html', html_data)

def form_choicefield_select_render(request):
    if request.method == 'POST':
        form_choicefield_select = FormChoiceFieldSelect(request.POST)
    else:
        form_choicefield_select = FormChoiceFieldSelect()

    html_data={'form_choicefield_select':form_choicefield_select}
    return render(request, 'forms_examples/form_choicefield_select.html', html_data)

def form_choicefield_flexible_render(request):
    """
    url: /forms/form_choice_flexible
    url shortcut: 'forms_examples:form_choice_flexible'

    Parameters
    ----------
    request : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    choices = [("",""),
                ("a","a"),
                ("b","b")]
    form_choice_flexible = FormChoiceFlexible(choices=choices)

    html_data={'form_choice_flexible':form_choice_flexible}
    return render(request, 'forms_examples/form_choice_flexible.html', html_data)

def form_choice_cascade(request):
    """
    url: /forms/form_choice_cascade
    url shortcut: 'forms_examples:form_choice_cascade'

    Parameters
    ----------
    request : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    if request.method == 'POST':
        form_choice_cascade = FormChoiceCascade(request.POST)
    else:
        form_choice_cascade = FormChoiceCascade()

    html_data = {'form_choice_cascade': form_choice_cascade}

    return render(request, 'forms_examples/form_choice_cascade.html', html_data)
