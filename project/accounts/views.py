from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login,logout
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
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
    template_name='accounts/user_login.html'
    def get_success_url(self):
        # login(self.request)
        return reverse_lazy('home')
    
class UserLogOutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')