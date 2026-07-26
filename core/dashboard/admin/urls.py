from django.urls import path , include
from . import views
app = "customer"
urlpatterns = [
    path("home/" , views.AdminDashboardHomeView.as_view() , name="home"),

]
