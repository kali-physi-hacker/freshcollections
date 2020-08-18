import os
import random
import uuid as _
from django.utils import timezone


RANDOM_LIMIT = 999999999


def get_file_name_ext(file_path):
    """
    Return the name and extension of a file a tuple
    :param file_path:
    :return:
    """
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def generate_random_name(title=None):
    """
    Generate and return a random name
    :param title:
    :return:
    """
    if title is None:
        title = ""
    random_name = f"{title}-{_.uuid4().hex}-{random.random(1, RANDOM_LIMIT)}"
    return random_name


def upload_path(instance, file_path):
    """
    Return a string for an upload path
    :param instance:
    :param file_path:
    :return:
    """
    file_name, ext = get_file_name_ext(file_path)
    random_name = f"{generate_random_name(file_name)}{ext}"
    final_name = f"products/{random_name}"
    return f"{timezone.now()}/products/{final_name}"
