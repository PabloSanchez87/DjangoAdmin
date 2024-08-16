from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
    
