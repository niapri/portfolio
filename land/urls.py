from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.update_list, name='update_list'),]
