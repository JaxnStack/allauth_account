# django_auth_plugin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="account_login"),
    path("signup/", views.CustomSignupView.as_view(), name="account_signup"),
    path("logout/", views.CustomLogoutView.as_view(), name="account_logout"),
    path("password/reset/", views.CustomPasswordResetView.as_view(), name="account_reset_password"),
    path("password/reset/done/", views.CustomPasswordResetDoneView.as_view(), name="account_reset_password_done"),
    path("password/change/", views.CustomPasswordChangeView.as_view(), name="account_change_password"),
    path("email/", views.EmailView.as_view(), name="account_email"),
    path("confirm-email/", views.ConfirmEmailView.as_view(), name="account_email_verification_sent"),
]
