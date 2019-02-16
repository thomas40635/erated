
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

from app.views import IndexView, ListMoviesView, LoginView, LogoutView, SignUpView, DetailMovieView, SearchFormView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index_view'),
    path('movies/', ListMoviesView.as_view(), name='list_movies_view'),
    re_path('^movies/letter/(?P<letter>\D+)', ListMoviesView.as_view(), name='list_movies_view'),
    path('movies/<int:pk>', DetailMovieView.as_view(), name='detail_movie_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('search/', SearchFormView.as_view(), name='search_form_view'),
]
