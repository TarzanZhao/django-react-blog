# from django.conf.urls import url
from django.urls import include, re_path
from .views import CategoryList

urlpatterns = [
    # List categories
    re_path(r'^categories/$', CategoryList.as_view()),
]

app_name = "categories"