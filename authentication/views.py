from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode
from django.http import JsonResponse
from django.urls import reverse

from authentication.forms import LoginForm, RegistrationForm, ProfileForm
from authentication.models import Profile
from authentication.utils import generate_activation_url
from authentication import constants
from authentication.utils import account_activation_token


# TODO: 1. Implement User Registration with Email Activation Link (AuthToken) generation
# TODO: 2. Implement Password Reset with Email Reset Link (PasswordResetToken) generation


User = get_user_model()


def auth_get(request):
    """
    Returns the template for user authentication (login/registration) - auth.html
    :param request:
    :return:
    """
    template = "authentication/auth.html"
    login_form = LoginForm()
    registration_form = RegistrationForm()
    context = {
        "login_form": login_form,
        "registration_form": registration_form
    }
    return render(request, template, context)


def login(request, user=None, next=None):
    """
    Authenticate and login a user, returning the homepage or a redirect(next) url
    :param request:
    :param user:
    :param next:
    :return:
    """
    if user:
        _login(request, user)
        if next:
            return redirect(next)
        else:
            return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            next_url = next or request.GET.get('next')
            if user is not None:
                _login(request, user)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect("home")
            else:
                messages.error(request, "Invalid username or password!")
                return redirect("authentication:auth_get")

    return redirect("authentication:auth_get")


def logout(request):
    """
    Log user out and clear all sessions
    :param request:
    :return:
    """
    _logout(request)
    next_url = request.GET.get("next")
    if next_url:
        return redirect(next_url)
    else:
        return redirect("home")


def register(request):
    """
    Sign up a user
    :param request:
    :return:
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        phone = request.POST.get("phone")
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get("username")
            user.set_password(form.cleaned_data.get("password1"))
            user.is_active = False
            user.save()
            profile = Profile.objects.create(
                user=user,
                telephone_number=phone
            )
            profile.save()
            url_name = "authentication:activate_user"
            activation_link = generate_activation_url(request, user, url_name)
            message_body = constants.ACCOUNT_ACTIVATION_MESSAGE.format(activation_link=activation_link)
            mailing_list = [user.email]
            send_mail("FreshCollections", message_body, "admin@freshcollections.com", mailing_list)
            user.backend = "authentication.backend.EmailAuthBackend"
            _login(request, user) # , backend="authentication.backend.EmailAuthBackend")
            next_url = request.GET.get("next")
            return redirect("authentication:registration_success")
        else:
            import pdb; pdb.set_trace();

    return redirect("authentication:auth_get")


def activate_user(request, uidb64, token):
    """
    Validate User token and activate user on clicking on activation link
    :param request:
    :param uidb64:
    :param token:
    :return:
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user.backend = "authentication.backend.EmailAuthBackend"
        _login(request, user)
        return redirect("authentication:activation-success")
    else:
        import pdb; pdb.set_trace()


def activation_success(request):
    """
    Return activation success page
    :param request:
    :return:
    """
    template = "authentication/activation-success.html"
    context = {}
    return render(request, template, context)


def registration_success(request):
    """
    Returns the template for the registration success page
    :param request:
    :return:
    """
    if request.user.is_anonymous:
        return redirect("authentication:auth_get")
    else:
        template = "authentication/registration-success.html"
        context = {}
        return render(request, template, context)


def forgot_password(request):
    template = "authentication/forgot-password.html"
    context = {}
    return render(request, template, context)


def reset_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            url_name = "authentication:change_password_page"
            password_reset_link = generate_activation_url(request, user, url_name)
            message_body = constants.PASSWORD_RESET_MESSAGE.format(email=email, password_link=password_reset_link)
            mailing_list = [email]
            send_mail("Password Reset Request", message_body, "admin@freshcollections.com", mailing_list)
            template = "authentication/password-link-sent.html"
            context = {}
            return render(request, template, context)
        except User.DoesNotExist:
            error_data = {
                "user_exist": False
            }
            return JsonResponse(error_data, safe=False, content_type="application/json")


def change_password_page(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (ValueError, TypeError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        template = "authentication/change-password.html"
        post_url = reverse("authentication:change_password", args=[uid])
        # import pdb; pdb.set_trace()
        context = {"post_url": post_url}
        return render(request, template, context)


def change_password(request, pk):
    if request.method == "POST":
        password = request.POST.get("password")
        user = User.objects.get(pk=pk)
        user.set_password(password)
        user.save()
        user.backend = "authentication.backend.EmailBackend"
        return login(request, user=user)

        # return redirect("home"


@login_required
def user_profile(request):
    template = "authentication/user-profile.html"
    profile = Profile.objects.get(user=request.user)
    context = {
        "profile": profile,
        "page_title": "Profile info",
        # "page_description": "Update your profile details below",
    }
    return render(request, template, context)


@login_required
def update_user_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.user is profile.user:
        form = ProfileForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password1")
            form.update()
            request.user.set_password(password)
        else:
            messages.error(request, "An Internal Server Error Occurred")
            return redirect("user-profile")

