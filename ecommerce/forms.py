from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    
    
