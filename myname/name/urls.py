
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('comment',views.comment , name='comment'),
    path('',views.home , name='home'),
    path('contact',views.contact , name='contact'),
    path('blog',views.blog , name='blog'),
    path('search',views.search , name='search'),
    path('login_user',views.login_user , name='login'),
    path('logout_user',views.logout_user , name='logout'),
    path('postblog',views.postblog , name='postblog'),
    path('signup',views.signup , name='signup'),
    path('postdetail/<str:slug>',views.postdetail , name='postdetail'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
