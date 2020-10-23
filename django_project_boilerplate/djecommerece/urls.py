from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('core/', include('core.urls', namespace='core')),
    path('subscribe/', include('subscribe.urls')),
    path('registration/', include('registration.urls')),
    path('upload/', include('profile_maker.urls')),
    path('ajax/', include('post.urls')),
    path('', include('home.urls')),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
