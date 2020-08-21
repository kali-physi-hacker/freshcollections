from django.urls import path

from authentication.views import (
    login, auth_get, logout, register, registration_success,
    forgot_password, user_profile, update_user_profile,
    activate_user, activation_success, reset_password, change_password_page,
    change_password, password_change_success
)


urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('auth/', auth_get, name="auth_get"),
    path('register/', register, name="register"),
    path('register-success/', registration_success, name="registration_success"),
    path('activate-user/<str:uidb64>/<str:token>/', activate_user, name="activate_user"),
    path('activation-success/', activation_success, name="activation-success"),
    path('forgot-password/', forgot_password, name="forgot_password"),
    path('reset-password/', reset_password, name="reset_password"),
    path('change-password/<int:pk>/', change_password, name="change_password"),
    path('change-password-page/<str:uidb64>/<str:token>/', change_password_page, name="change_password_page"),
    path('password-change-success/', password_change_success, name="password_change_success"),
    path('profile/', user_profile, name="user_profile"),
    path('update-user-profile/', update_user_profile, name="update_user_profile")
]

app_name = "authentication"
