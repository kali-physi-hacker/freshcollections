from django import forms
from django.contrib.auth import get_user_model

from authentication.models import Profile


User = get_user_model()


class LoginForm(forms.Form):
    """
    Form for user login validation
    """
    username = forms.EmailField()
    password = forms.CharField()


class RegistrationForm(forms.ModelForm):
    """
    Form for user registration validation
    """
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        """
        Return any of the passwords if password1 and password2 are equal,
        Raise ValidationError otherwise
        :return:
        """
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Passwords don't match")

        return data['password1']


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    photo = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=14)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)

    def clean_password1(self):
        """
        Valid Passwords and make sure they're equal
        :return:
        """
        data = self.cleaned_data
        if data.get("password1") or data.get("password2"):
            if data.get("password1") != data.get("password2"):
                return False
        return True

    def update(self):
        profile = Profile.objects.update(
            telephone_number = self.cleaned_data.get("phone_number"),
            photo=self.cleaned_data.get("photo")
        )
        profile.save()
