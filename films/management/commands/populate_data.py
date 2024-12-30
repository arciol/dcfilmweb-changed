from django.core.management.base import BaseCommand
from films.models import Film
from django.contrib.auth.models import User
from faker import Faker
import random


class Command(BaseCommand):
    help = "Populates the database with fake data"

    def handle(self, *args, **options):
        fakegen = Faker()

        for _ in range(80):
            movie = Film()
            movie.title = fakegen.name()
            movie.description = fakegen.text()
            movie.added_by = random.choice(User.objects.all())
            movie.director = fakegen.name()
            movie.year = random.randint(2000, 2021)

            movie.save()
