from django.conf.urls import include, url
from django.contrib import admin
from fourth_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'fourth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^$', views.index, name="welcome"),
    
]
