from django.contrib.auth import get_user_model


User = get_user_model()


class EmailAuthBackend(object):
    """
    Authenticate using e-mail address
    """
    def authenticate(self, request, username=None, password=None):
        """
        Overriding this method to make users authenticate using their emails
        :param request:
        :param username:
        :param password:
        :return:
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Returns a user with a specified user_id
        :param user_id:
        :return:
        """
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None
