from django.shortcuts import  redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission

class AdminDashboardHomeView(TemplateView,LoginRequiredMixin,HasAdminAccessPermission):
    template_name = 'dashboard/admin/home.html'