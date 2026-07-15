from django.shortcuts import render
from django.contrib.auth import views as auth_views
from  accounts.forms import AuthenticationForm
class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = "accounts/login.html" 
    redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView):
    pass