from django.conf.urls import url
from .views import SchemaView


urlpatterns = [
    url(r'^Schema', SchemaView.as_view(), name='application'),
]