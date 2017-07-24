from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^users$', views.index_and_create),
    url(r'^users/new$', views.users_new),
    url(r'^users/(?P<user_id>\d+)$', views.users_show_and_update),
	url(r'^users/(?P<user_id>\d+)/edit$',views.users_edit),
	url(r'^users/(?P<user_id>\d+)/destroy$',views.users_delete)

]
