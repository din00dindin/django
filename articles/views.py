from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
from django.template import loader

def index(request):
    latest_Articles_list = Articles.objects.all
    template = loader.get_template("articles/index.html")
    context = {"latest_Articles_list": latest_Articles_list}
    return HttpResponse(template.render(context, request))

def detail(request, Articles_id):
    return HttpResponse("You're looking at Articles %s." % Articles_id)