from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage' ),
    path('home/', views.home, name = 'homepage' ),
    path('about_us/', views.about, name = 'aboutpage' ),
    path('contact_us/', views.contact, name = 'contactpage' ),
    path('dashboard/authentication/user/login/', views.login_page, name = 'login_page' ),
    path('dashboard/authenticated/user/home/', views.dashboard_home, name = 'dashboard_home' ),
    path('dashboard/property/add/', views.add_property, name = 'add_property' ),
    path('dashboard/property/list/', views.property_list, name = 'property_list' ),
    path('dashboard/property/add/land/', views.add_property_land, name = 'add_property_land' ),
    path('dashboard/property/add/house/', views.add_property_house, name = 'add_property_house' ),
    path('dashboard/property/add/appartment/', views.add_property_appartment, name = 'add_property_appartment' ),
    path('dashboard/property/list/land/', views.property_list_land, name = 'property_list_land' ),
    path('dashboard/property/list/house/', views.property_list_house, name = 'property_list_house' ),
    # path('dashboard/property/edit/', views.edit_property, name = 'edit_property' ),
    path('dashboard/authentication/user/logout/', views.logout_page, name = 'logout' ),
    path('category/residential/house/', views.residential_house, name = 'residential_house' ),
    path('category/land/', views.land_list, name = 'land_list' ),
]
