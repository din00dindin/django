from django.shortcuts import render
from .models import Contact

def contact_view(request):
    return render(request, "contact_us/contact.html")
