"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import pkg_resources
from django.urls import path, include
from django.contrib import admin


def load_plugins_url(group_id):
    paths = []
    for ep in pkg_resources.iter_entry_points(group=group_id):
        if str(ep).split('=')[0].strip() == 'path':
            paths.append(str(ep).split('=')[1].strip())
    return paths


PLUGINS_URL = set(load_plugins_url('urls'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_app.urls')),
]

for url in PLUGINS_URL:
    urlpatterns.append(path("", include(url)))
