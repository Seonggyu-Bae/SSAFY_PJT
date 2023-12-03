from django.urls import path
from . import views


urlpatterns = [
    path('', views.user),
    path('list/', views.user_list),
    path('add_product/<int:user_id>/', views.add_product),
    path('update_product/<int:user_id>/', views.update_financial_products),

]
