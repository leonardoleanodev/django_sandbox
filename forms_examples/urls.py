from django.urls import path
from forms_examples import views

app_name = 'forms_examples'

urlpatterns = [
    path("sample", views.view_sample, name='http_reponse_sample'),
    path("form_charfield_render", views.form_charfield_render, name='form_charfield_render'),
    path("form_choicefield_select_render",views.form_choicefield_select_render, name='form_choicefield_select'),
    path("form_choice_flexible",views.form_choicefield_flexible_render, name='form_choice_flexible'),
]