from django.contrib import admin

from .models import Question
from .models import Account

admin.site.register(Question)
admin.site.register(Account)
