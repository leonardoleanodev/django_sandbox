from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def csrf_index(request):
    html_data={}
    return render(request, "csrf_protection/index.html",html_data)

@csrf_exempt
def without_protection(request):
    """
    without_protection

    url: csrf/without_protection/
    url-shortcut: "csrf_protection:without_protection"

    Parameters
    ----------
    request : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    html_data={}
    return render(request, "csrf_protection/index.html", html_data)

def with_standard_protection(request):
    """
    without_protection

    url: csrf/without_protection/
    url-shortcut: "csrf_protection:with_standard_protection"

    Parameters
    ----------
    request : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    html_data={}
    return render(request, "csrf_protection/index.html", html_data)
