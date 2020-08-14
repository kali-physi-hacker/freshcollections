import os
import random
import uuid as _

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes

RANDOM_UPPER_LIMIT = 999999999


def get_filename_ext(file_path):
    """
    Rturn the filename and extension of a full file name.
    :param file_path:
    :return:
    """
    file_base = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(file_base)
    return file_name, file_ext


def upload_path(inst, filename):
    """
    Return a random name for saving the file
    :param inst:
    :param filename:
    :return:
    """
    file_name, file_ext = get_filename_ext(filename)
    random_file_name = random.randint(1, RANDOM_UPPER_LIMIT)
    final_file_name = f"{random_file_name}{_.uuid4()}{file_ext}"
    return f"profile_photos/{random_file_name}/{final_file_name}"


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk)+six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


def generate_activation_url(request, user, url_name):
    _token = account_activation_token.make_token(user)
    current_site = get_current_site(request)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    # activation_link = f"{url_base}/{uid}/{_token}"
    activation_link = current_site.domain + reverse(url_name, args=[uid, _token])
    return activation_link
