from django.contrib import admin
from .models import Contract, User


admin.site.register(Contract),
admin.site.register(User)