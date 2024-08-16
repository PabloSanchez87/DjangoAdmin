from django import forms

# Create your forms here.
class SearchForm(forms.Form):
    query = forms.CharField(
        label='Buscar',
        max_length=100
    )