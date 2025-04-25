from django.urls import path, re_path
from apps.securities import views

urlpatterns = [

    # The home page
    path("", views.securities_view, name='securities_view'),

    # Route for securities.html
    path("securities/add/", views.securities_add, name="securities_add"),
    path("securities/edit/", views.securities_edit, name="securities_edit"),
    path("securities/search/", views.securities_search, name="securities_search"),
    path("securities/delete/<int:id>/", views.securities_delete, name="securities_delete"),
]
