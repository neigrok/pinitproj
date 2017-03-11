from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.views import View
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
class Login(View):
    def get(self, request):
        form = LoginUserForm()
        return render(request, 'primitive_registration/login.html', {'form': form})

    def post(self, request):
        username = request.POST.get('login')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Incorrect login or password')
            return redirect('/login')


class Register(View):
    def get(self, request):

        form = CreateUserForm()
        return render(request, 'primitive_registration/registration.html', {'form': form})

    def post(self, request):
        user = None
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                password = form.clean_password2()
                ulogin = form.cleaned_data['login']
                user = User.objects.create_user(ulogin, None, password)
            except IntegrityError:
                    messages.add_message(request, messages.INFO, 'This username is already taken')
                    form = CreateUserForm(request.POST)
                    return render(request, 'primitive_registration/registration.html', {'form': form})
        else:
            messages.add_message(request, messages.INFO, 'Password mismatch')

        if user:
            messages.add_message(request, messages.SUCCESS, 'Registration successful. Please, sign in')
            return redirect('../login')
        else:
            return redirect('/register')

def logout_view(request):
    logout(request)
    return redirect('../')