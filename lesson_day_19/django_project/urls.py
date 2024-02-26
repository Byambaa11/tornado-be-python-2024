
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"),
       name="home"),
    path('', include('pages.urls')),
    path("accounts/", include("accounts.urls")),
    path("", include("blog.urls")),
    path('__reload__', include('django_browser_reload.urls')),
]


