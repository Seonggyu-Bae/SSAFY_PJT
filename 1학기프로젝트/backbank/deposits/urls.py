from django.urls import path, include
from . import views



urlpatterns = [
    path('deposits/', views.deposit_index),
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    path('deposit-product-options/', views.deposit_product_options),
    # path('deposit-products/top_rate/', views.top_rate),

    path('savings/', views.saving_index),
    path('save-saving-products/', views.save_saving_products),
    path('saving-products/', views.saving_products),
    path('saving-product-options/', views.saving_product_options),

]
