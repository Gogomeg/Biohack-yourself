from django.contrib import admin
from .models import Hack

# Register your models here.


@admin.register(Hack)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "hack_type",
        "content",
        "image",
    )
    list_filter = ("hack_type",)
