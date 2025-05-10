from allauth.account.views import (
    LoginView,
    SignupView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    ConfirmEmailView as AllauthConfirmEmailView,
    EmailView as AllauthEmailView
)

from django.urls import reverse_lazy
from django.views.generic import TemplateView


class CustomLoginView(LoginView):
    template_name = "account/login.html"
    success_url = reverse_lazy("account_email")


class CustomSignupView(SignupView):
    template_name = "account/signup.html"
    success_url = reverse_lazy("account_email")


class CustomLogoutView(LogoutView):
    template_name = "account/logout.html"


class CustomPasswordResetView(PasswordResetView):
    template_name = "account/password_reset.html"
    email_template_name = "account/password_reset_email.html"
    success_url = reverse_lazy("account_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "account/password_reset_done.html"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "account/password_change.html"
    success_url = reverse_lazy("account_email")


class EmailView(AllauthEmailView):
    template_name = "account/email.html"


class ConfirmEmailView(AllauthConfirmEmailView):
    template_name = "account/email_confirm.html"
