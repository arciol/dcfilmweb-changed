from django.contrib import admin
from .models import Film


# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
        "director",
        "category",
        "average_rating",
        "created_at",
        "updated_at",
    )
    fields = (
        "title",
        "year",
        "director",
        "category",
        "created_at",
        "updated_at",
        "average_rating",
        "added_by",
        "want_to_watch",
        "watched",
    )
    readonly_fields = ("created_at", "updated_at", "average_rating")


admin.site.register(Film, FilmAdmin)
