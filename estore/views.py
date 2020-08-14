from django.shortcuts import render

from authentication.forms import LoginForm, RegistrationForm


def home(request):
    """
    Return the landing page of the app
    :param request:
    :return:
    """
    template = "index.html"
    login_form = LoginForm()
    registration_form = RegistrationForm()
    context = {
        "login_form": login_form,
        "registration_form": registration_form
    }
    return render(request, template, context)
