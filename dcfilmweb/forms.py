from dataclasses import fields
from urllib import request
from django.forms import ModelForm
from films.models import Film
from ratings.models import Rating


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ["title", "year", "director", "description"]


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]
