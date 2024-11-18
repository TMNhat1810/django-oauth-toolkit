from django.contrib import admin
from django.urls import include, path
from oauth2_provider import urls as oauth2_urls

from .app.views import GroupList, UserDetails, UserList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include(oauth2_urls)),
    path("users/", UserList.as_view()),
    path("users/<pk>/", UserDetails.as_view()),
    path("groups/", GroupList.as_view()),
]
