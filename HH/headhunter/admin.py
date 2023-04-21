from django.contrib import admin
from .models import Vacancy, Resume, Response, Message

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Resume)
admin.site.register(Response)
admin.site.register(Message)
