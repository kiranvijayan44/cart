from django.urls import path
from . import views

app_name = 'bag'

urlpatterns = [
    path('add/<int:product_id>/', views.add_bag, name='add_bag'),
    path('', views.bag_detail, name='bag_detail'),
    path('remove/<int:product_id>', views.bag_remove, name='bag_remove'),
    path('delete/<int:product_id>', views.bag_delete, name='bag_delete'),

]