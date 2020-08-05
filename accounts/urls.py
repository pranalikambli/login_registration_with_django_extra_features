from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name="sign_up"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('login', auth_views.LoginView.as_view(),{'template_name': 'registration/login.html'}, name='login'),
    # Change Password
    path(
        'change-password/',auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url='/'
        ),name='change_password'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html',
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
         ),name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_mail_sent.html'
         ),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirmation.html'
         ),name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_completed.html'
         ),name='password_reset_complete'),
]