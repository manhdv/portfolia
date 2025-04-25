from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Route for securities.html
    path("securities/add/", views.securities_add, name="securities_add"),
    path("securities/edit/", views.securities_edit, name="securities_edit"),
    path('securities.html', views.securities_view, name='securities_view'),
    path("securities/search/", views.securities_search, name="securities_search"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
