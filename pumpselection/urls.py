"""pumpselection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pumpselection.view import views
from pumpselection.view.views import search_sql_files

urlpatterns = [
    path('my_view/', views.my_view, name='my_form_view'),
    path('my_view/sales', views.my_view_sales, name='my_form_view_sales'),
    path('my_view/cus', views.my_view_cus, name='my_form_view_cus'),
    # path('form/', views.my_view, name='my_form_view'),
    path('admin/', admin.site.urls),
    path('table/', views.read_table, name='read_table'),
    path('table/sales', views.read_table_sales, name='read_table_sales'),
    path('user/', views.read_user, name='read_user'),

    path('details/<str:fac_number>/', views.show_details, name='details'),

    path('table/details/sales/<str:fac_number>', views.show_details_sales, name='details_sales'),


    path('details_user/<str:user_name>/', views.show_details_user, name='uesr_details'),

    # path('search/', views.employee_search, name='search'),
    path('signup/',views.signup, name='signup'),

    path('',views.login, name='login'),
    path('update/<str:fac_number>/', views.update, name='update'),
    path('sales/update/<str:fac_number>/', views.update_sales, name='update'),
    path('delete/<str:fac_number>/', views.delete, name='delete'),

    path('table/details/sales/delete/<str:fac_number>/sales', views.delete_sales, name='delete_sales'),

    path('user_delete/<str:user_name>/', views.user_delete, name='user_delete'),
    path('adddata/',views.add_data, name='add_data'),
    path('adddata/sales',views.add_data_sales, name='add_data_sqles'),
]
