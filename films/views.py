import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from films.models import Film
from ratings.models import Rating
from dcfilmweb.forms import FilmForm
from django.http import JsonResponse

# Create your views here.


@login_required(login_url="/oauth2/login")
def dashboard(request):
    films_list = Film.objects.all().order_by("-created_at")
    watched_films = request.user.films_watched.all().order_by("-updated_at")
    added_films = request.user.films_added.all().order_by("-created_at")
    watchlist = request.user.films_to_watch.all()
    return render(
        request,
        "dashboard.html",
        {
            "films": films_list,
            "watched_films": watched_films,
            "added_films": added_films,
            "current_user": request.user,
            "watchlist": watchlist,
        },
    )


def films(request):
    films_list = Film.objects.all().order_by("-created_at")
    return render(
        request,
        "films_all.html",
        {
            "films": films_list,
            "current_user": request.user,
        },
    )


def film_add(request):
    form = FilmForm(request.POST or None)
    if form.is_valid():
        film = form.save(commit=False)
        film.added_by = request.user
        film.save()
        return redirect("/")
    return render(request, "add_film.html", {"form": form})


def film_delete(request, id):
    film = Film.objects.get(id=id)
    film.delete()
    return redirect("/")


def film_edit(request, id):
    film = Film.objects.get(id=id)
    form = FilmForm(request.POST or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "add_film.html", {"form": form, "film": film})


def film_rate(request, id):
    film = Film.objects.get(id=id)
    if film not in request.user.films_watched.all():
        return JsonResponse(
            {"status": "error", "message": "You have to watch the film"}
        )
    if request.method == "POST":
        rating = request.POST.get("rating")
        if film.has_user_rated(request.user):
            film_rating = Rating.objects.get(user=request.user, film=film)
            film_rating.rating = rating
            film_rating.save()
        else:
            film_rating = Rating.objects.create(
                user=request.user, film=film, rating=rating
            )
            film_rating.save()
    return JsonResponse(
        {"status": "success", "new_average_rating": film.average_rating()}
    )


def wanna_watch(request, id):

    film = Film.objects.get(id=id)
    if request.user in film.want_to_watch.all():
        film.want_to_watch.remove(request.user)
    else:
        film.want_to_watch.add(request.user)
    users_want_to_watch = [user.username for user in film.users_want_to_watch()]
    watchlist_films = list(request.user.films_to_watch.all().values())
    return JsonResponse(
        {
            "status": "success",
            "users_want_to_watch": users_want_to_watch,
            "watchlist": watchlist_films,
        }
    )
