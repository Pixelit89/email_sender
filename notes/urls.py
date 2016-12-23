from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'add_note/$', views.add_note, name='add_note'),
    url(r'del_note_(?P<note_id>[0-9]+)/$', views.del_note, name='del_note'),
    url(r'send_mail_(?P<mail_to>[a-zA-Z0-9\W]+)/', views.send, name='send_mail'),
]