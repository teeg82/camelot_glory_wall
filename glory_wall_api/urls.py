from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.glory_wall_post)
]