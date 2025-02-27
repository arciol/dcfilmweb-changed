from django.contrib import admin
from .models import Rating


# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ("film", "rating", "user", "created_at", "updated_at")
    fields = ("film", "rating", "user", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Rating, RatingAdmin)
