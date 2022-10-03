# from django.conf.urls import url
from django.urls import include, re_path

from .views import SettingsDetail

urlpatterns = [
    re_path(r'^settings/$', SettingsDetail.as_view()),
]

app_name = "core"