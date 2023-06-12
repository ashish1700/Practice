
from django.contrib import admin
from django.urls import path
from app1 import views
# from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage, name='signup'),
    path('login/',views.LoginPage, name='login' ),
    path('home/',views.HomePage, name='home' ),
    path('logout/',views.LogoutPage,name='logout'),

    # path('upload/', upload_video, name='upload_video'),
    # path('watch/<int:video_id>/', watch_video, name='watch_video'),
]


