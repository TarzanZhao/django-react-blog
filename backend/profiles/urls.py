# from django.conf.urls import url
from django.urls import include, re_path

from .views import SubscriberCreate

urlpatterns = [
    # Create post
    re_path(r'^subscribe$', SubscriberCreate.as_view()),
]

app_name = "core"