from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login,logout
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
class UserRegistrationView(FormView):
    template_name='accounts/user_registration.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('register')
    def form_valid(self,form):
        print(form.cleaned_data)
        # user=form.save()
        # login(user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):