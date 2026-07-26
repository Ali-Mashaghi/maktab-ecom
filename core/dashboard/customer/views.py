from django.shortcuts import  redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
class CustomerDashboardHomeView(TemplateView,LoginRequiredMixin,HasCustomerAccessPermission):
    template_name = 'dashboard/customer/home.html'