from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, ListView, FormView, CreateView

from app.models import Film
from erated import settings


class IndexView(TemplateView):
    template_name = 'index.html'


class ListMoviesView(ListView):
    model = Film
    template_name = 'list_movies.html'


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


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index_view')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

