from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='index'),
    path('add_stocks/', add_stocks, name='add_stocks'),
    path('update_stocks/<product_id>', update_stocks, name='update_stocks'),
    path('delete-stock/<product_id>', delete_stock, name='delete-stock'),
    # path('add-del-qty/', add_del_quantity, name='add-del-qty'),
    path('login_user/', login_user, name='login'),
    path('logout_user/', logout_user, name='logout'),
    path('signup/', register_user, name='signup'),
    path('category/<int:category_id>/<str:category_title>/', categories, name='category_detail'),
    path('add_qty/', add_qty, name='add_qty'),

]