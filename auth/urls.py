 
from django.urls import path
from auth.views import signup,logoutfunction
from django.contrib.auth import views
 
urlpatterns = [
    #Authentication mean singn up,login and logout
    path('signup/', signup,name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',  logoutfunction, name='logout'),
    #Password recovery :we use django builtin password recovery system
    #this func url render the pg that contain email field to send email 
    path("password_reset/", views.PasswordResetView.as_view(template_name='reset_password.html'), name="password_reset"),
    #this func url displays a confirmation msg that email has sent 
    
    path(
        "password_reset_done/",
        views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
        name="password_reset_done",
    ),
    #this func url provide unique token that contain link in an email that django sent , link conatin fields to reset password
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(template_name='password_set.html'),
        name="password_reset_confirm",
    ),
    #this func url display confirmation msg that your password resets 
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
        name="password_reset_complete",
    ),

]
