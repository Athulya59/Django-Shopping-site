from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
	path('',views.home,name='home'),
	path('signup/',views.signup,name='signup'),
	path('login/',views.login,name='login'),
	path('products/',views.products,name='products'),
]

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)