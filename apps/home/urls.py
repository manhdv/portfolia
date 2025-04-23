# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Route for securities.html
    path("securities/add/", views.add_stock, name="add_stock"),
    path("securities/edit/", views.edit_stock, name="edit_stock"),
    path('securities.html', views.securities_view, name='securities'),
    path('user.html', views.user_profile_view, name='user'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
