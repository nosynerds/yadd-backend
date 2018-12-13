from django.conf.urls import url
from .views import SchemaView, TableView, ColumnView


urlpatterns = [
    url(r'^Schema', SchemaView.as_view(), name='application'),
    url(r'^Table', TableView.as_view(), name='application'),
    url(r'^Column' , ColumnView.as_view() , name='application') ,
]