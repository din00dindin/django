from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_lenght=100, label = "Name")
    email = forms.EmailField(label = "email")
    message = forms.CharField(widget = forms.Textarea, label = "message")