from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth import login,logout
from .forms import UserRegistrationForm,UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class UserRegistrationView(generic.FormView):
    template_name='accounts/user_registration.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('register')
    def form_valid(self,form):
        print(form.cleaned_data)
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    def get_success_url(self):
        # login(self.request)
        return reverse_lazy('home')
    
class UserLogOutView(generic.View):
    def get(self,r):
        logout(r)
        return redirect('home')


class UserBankAccountUpdateView(generic.View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})