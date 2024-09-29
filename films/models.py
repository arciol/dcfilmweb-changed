from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


# Create your models here.
class Film(models.Model):
    DRAMA = "Dramat"
    HORROR = "Horror"
    THRILLER = "Thriller"
    COMEDY = "Komedia"
    CATEGORY_CHOICES = [
        (DRAMA, "Drama"),
        (HORROR, "Horror"),
        (THRILLER, "Thriller"),
        (COMEDY, "Comedy"),
    ]
    title = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()
    director = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES, default=DRAMA)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="films_added", null=True
    )
    want_to_watch = models.ManyToManyField(
        User, related_name="films_to_watch", blank=True, null=True
    )
    watched = models.ManyToManyField(
        User, related_name="films_watched", null=True, blank=True
    )

    def __str__(self):
        return self.title

    def average_rating(self):
        try:
            return round(self.film_ratings.aggregate(Avg("rating"))["rating__avg"], 2)
        except:
            return None

    def has_user_rated(self, user):
        return self.film_ratings.filter(user=user).exists()

    def users_want_to_watch(self):
        return self.want_to_watch.all()

    def users_watched(self):
        return self.watched.all()
