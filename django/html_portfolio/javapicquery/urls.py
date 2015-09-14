from django.conf.urls import include, url
from javapicquery import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.javapicqueryindex, name='home'),
    url(r'^join', views.javapicqueryjoin, name='join'),
    url(r'^gallery', views.javapicquerygallery, name='gallery'),

]