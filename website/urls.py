from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('project/', project, name='project'),
    path('contact/', contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
