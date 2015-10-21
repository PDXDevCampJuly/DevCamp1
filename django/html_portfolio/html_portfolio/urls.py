from django.conf.urls import include, url



urlpatterns = [
    # Examples:
    # url(r'^$', 'html_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^about/', include("about.urls")),
    url(r'^_me/', include("about.urls")),
    url(r'^javapic/', include("javapic.urls")),
    url(r'^javapicquery/', include("javapicquery.urls")),
    url(r'^zen_mockup/', include("zen_mockup.urls")),
    url(r'^forum/', include("forum.urls")),


]
