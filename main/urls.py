from django.urls import path
from . import views

urlpatterns = [
path('all_list/', views.all_lists, name='all_lists'),
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
]

