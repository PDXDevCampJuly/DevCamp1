from django.conf.urls import include, url
from javapicquery import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.indexjq, name='index'),
    url(r'^join', views.joinjq, name='join'),
    url(r'^gallery', views.galleryjq, name='gallery'),

]