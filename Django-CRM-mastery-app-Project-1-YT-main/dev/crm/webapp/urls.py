
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),
    
    path('sales-overview/', views.sales_overview, name='sales-overview'), 

    # CRUD

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),

    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    
     path('interaction-tracking/', views.interaction_tracking, name='interaction-tracking'),
    path('sales-management/', views.sales_management, name='sales-management'),
    path('service-management/', views.service_management, name='service-management'),
]






