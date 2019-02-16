from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView

from app.forms.SearchForm import SearchForm
from app.models import Film
from erated import settings


class IndexView(TemplateView):
    template_name = 'index.html'


class ListMoviesView(ListView):
    model = Film
    template_name = 'list_movies_letter.html'

    def get_context_data(self, **kwargs):
        result = super(ListMoviesView, self).get_context_data(**kwargs)
        result['letters'] = [chr(a) for a in range(ord('A'), ord('Z') + 1)]
        letter = self.kwargs.get('letter', False)
        if letter is not False:
            result['selectedLetter'] = self.kwargs['letter']
        return result

    def get_queryset(self, *args):
        letter = self.kwargs.get('letter', False)
        if letter is not False:
            posts = Film.objects.filter(
                Q(titre__startswith=self.kwargs['letter']) | Q(titre__startswith=self.kwargs['letter'].upper()))
        else:
            posts = Film.objects.all()
        return posts


class DetailMovieView(DetailView):
    model = Film
    template_name = 'detail_movie.html'


class LoginView(LoginView):
    template_name = 'login.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login_view')
    template_name = 'signup.html'


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'list_movies_by_search.html'

    def get_initial(self):
        initial = super(SearchFormView, self).get_initial()
        initial['titre'] = 'QUELQUE CHOSE'
        return initial

    def get_success_url(self):
        return reverse('cocktail_list_by_name',
                       kwargs={'word': self.request.POST['titre']})

    def form_valid(self, form):
        return super(SearchFormView, self).form_valid(form)

