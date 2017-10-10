from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from .models import Evenement

# Apply summernote to all TextField in model.
class EvenementAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("naam",)}
    pass
admin.site.register(Evenement, EvenementAdmin)
