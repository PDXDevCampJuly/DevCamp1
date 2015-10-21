from django.conf.urls import include, url
from javapic import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.javapicindex, name='homejavapic'),
    url(r'^join', views.javapicjoin, name='join'),
    url(r'^gallery', views.javapicgallery, name='gallery'),
]
