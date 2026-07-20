from django.urls import path ,re_path
from . import views
app_name ="shop"
urlpatterns = [
    path('product/grid/', views.ShopProductGridView.as_view(),name = "product_grid"),
    re_path(r'(?P<slug>[^/]+)/?$', views.ShopProductDetailView.as_view(), name="post_detail"),
]