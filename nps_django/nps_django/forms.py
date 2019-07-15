from django import forms

class PassholderForm(forms.Form):
  first_name = forms.CharField(label="First name:", max_length=200)