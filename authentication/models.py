from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

class LocationData(models.Model):
    address = models.CharField(max_length=1024, default=None, null=True)
    city = models.CharField(max_length=50, default=None, null=False)
    state = models.CharField(max_length=10, default=None, null=True)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, default=None, null=True
    )
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, default=None, null=True
    )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    size = models.FloatField(_('size'))

    LEFT_FOOT = "L"
    RIGHT_FOOT = "R"

    PAIR_OPTIONS = [(LEFT_FOOT, "Left foot"),(RIGHT_FOOT, "Right foot")]

    pair = models.CharField(_('pair'), choices=PAIR_OPTIONS, max_length=1)

    MALE_CLOTHING_PREFERENCE = "M"
    FEMALE_CLOTHING_PREFERENCE = "F"
    ANY = "A"

    PREFRENCE_OPTIONS = [(MALE_CLOTHING_PREFERENCE, "Male presenting clothing"), (FEMALE_CLOTHING_PREFERENCE, "Female presenting clothing"), (ANY, "Any")]

    clothing_preference = models.CharField(_('user preference'), choices=PREFRENCE_OPTIONS, default=ANY, max_length=1)

    location = models.OneToOneField(LocationData, on_delete=models.SET_NULL, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)