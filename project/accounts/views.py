from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login,logout
from .forms import UserRegistrationForm
# Create your views here.
class UserRegistrationView(FormView):
    template_name=''
    form_class=UserRegistrationForm
    success_url=''
    def form_valid(self, form):
        user=form.save()
        login(user)
        return super().form_valid(form)