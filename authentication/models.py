from django.db import models

from authentication.utils import upload_path


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    telephone_number = models.CharField(max_length=14, null=True)
    photo = models.ImageField(upload_to=upload_path, blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - <{self.user.email}>"
