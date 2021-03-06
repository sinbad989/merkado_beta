from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.home, name='home'),

	url(r'^products/$',views.product_list, name='product_list'),
	url(r'^about/$',views.about, name='about'),
	url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name = 'product_list_by_category'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail, name='product_detail'),
	

]