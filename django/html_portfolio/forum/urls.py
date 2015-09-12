from django.conf.urls import include, url
from about import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='toc'),
    url(r'^join.html', views.javapicprettiness, name='JavaPic!'),
    url(r'^mock_up.html', views.zen_mockery, name='MockUpery'),
    url(r'^forum.html', views.forumfun, name='FunForum')

]
