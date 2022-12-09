from django.urls import path
from . import views

app_name = 'cartapp'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='Products_By_Category'),
    path('<slug:c_slug>/<slug:product_slug>', views.proDetail, name='Product_Category_Detail'),

]