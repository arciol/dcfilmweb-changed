"""
URL configuration for dcfilmweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
import discordlogin.views
import films.views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", films.views.dashboard, name="dashboard"),
    path("films/", films.views.films, name="films"),
    path("me/", discordlogin.views.user_data, name="me"),
    path("add_film/", films.views.film_add, name="add_film"),
    path("edit_film/<int:id>/", films.views.film_edit, name="edit_film"),
    path("delete_film/<int:id>/", films.views.film_delete, name="delete_film"),
    path("rate_film/<int:id>/", films.views.film_rate, name="rate_film"),
    path("wanna_watch/<int:id>/", films.views.wanna_watch, name="wanna_watch"),
    path("admin/", admin.site.urls),
    path("oauth2/login/", discordlogin.views.discord_login, name="oauth2_login"),
    path(
        "oauth2/login/redirect/",
        discordlogin.views.discord_login_redirect,
        name="discord_login_redirect",
    ),
    path("logout/", discordlogin.views.logout_view, name="logout"),
]
