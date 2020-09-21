from django.conf.urls import url
from api.views import pharacter_list, pharacter_detail

urlpatterns = [
    url(r'^Pharacter/$', pharacter_list),
    url(r'^Pharacter/(?P<pk>[0-9]+)/$', pharacter_detail),
]
