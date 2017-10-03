from django.conf.urls import url
from eventex.subscriptions.views import detail
from eventex.subscriptions.views import new


urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(\d+)/$', detail, name='detail'), #TODO: M3A05 - trocar para UUID
]
