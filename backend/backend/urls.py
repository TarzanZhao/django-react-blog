"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import include
from rest_framework.authtoken import views
from django.urls import include, re_path
from posts import urls as posts_urls

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^rest-api-auth/', include('rest_framework.urls',
                                    namespace='rest_framework')),
    re_path(r'^api/v1/auth/', views.obtain_auth_token),

    re_path(r'^api/v1/', include('posts.urls', namespace='posts')),
    re_path(r'^api/v1/', include('categories.urls', namespace='categories')),
    re_path(r'^api/v1/', include('core.urls', namespace='core')),
    re_path(r'^api/v1/', include('profiles.urls', namespace='core')),

    re_path(r'', include(posts_urls)),    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

