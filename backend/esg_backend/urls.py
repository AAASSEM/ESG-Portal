"""
URL configuration for esg_backend project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import react_app_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    # Serve React app for all other routes
    path('', react_app_view, name='react_app'),
    path('onboard/', react_app_view, name='react_app'),
    path('rame/', react_app_view, name='react_app'),
    path('list/', react_app_view, name='react_app'),
    path('meter/', react_app_view, name='react_app'),
    path('data/', react_app_view, name='react_app'),
    path('dashboard/', react_app_view, name='react_app'),
    # Catch-all pattern for any other React routes
    re_path(r'^.*/$', react_app_view, name='react_app_catchall'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)