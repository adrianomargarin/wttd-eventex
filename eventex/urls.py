from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from eventex.core.views import home
from eventex.core.views import speaker_detail
from eventex.subscriptions.views import detail


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', speaker_detail, name='speaker_detail'),
    url(r'^admin/', admin.site.urls),
]
