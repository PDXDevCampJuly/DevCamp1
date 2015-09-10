from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.index, name='index'),
    url(r'^hello/', include('hello.urls'))
]
