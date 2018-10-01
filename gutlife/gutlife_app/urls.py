from django.conf.urls import url

from . import views

urlpatterns = [
    url('dashboard/', views.index, name='main'),
    url('api/data/', views.get_data),
    url('bm-log/', views.post),
    url('accounts/create_account/', views.adduser, name='create_account'),
]