from django import forms

class FormCharField(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class FormChoiceFieldSelect(forms.Form):
    choices = [('',''),
               ('first','1o'),
               ('second','2o')
               ]
    select_options = {
        'class':'form-choices-field-select',
        'data-placeholder': 'first-value'
        }
    example_choice = forms.ChoiceField(
        choices = choices, 
        widget=forms.Select(select_options)
        )

class FormChoiceFlexible(forms.Form):
    def __init__(self, choices=[("a","a")]):
        super(FormChoiceFlexible, self).__init__()
        self.fields['example_form_choice_flexible'] = forms.ChoiceField(
            choices=choices
            )