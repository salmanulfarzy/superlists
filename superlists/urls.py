from django.conf.urls import url
from django.contrib import admin
from lists import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/the-only-list-in-the-world/$', 
        views.view_list, name='view_list'),
]

