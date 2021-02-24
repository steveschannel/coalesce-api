from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, pair, size, preference, **extra_fields):
        """
        Creates, saves a user with passed email and password.
        """
        if not email:
            raise ValueError(_('Email is required and must be set.'))
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.pair = pair
        user.size = size
        user.clothing_preference = preference
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, pair=None, size=None, preference=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, pair, size, preference, **extra_fields)

    def create_superuser(self, email=None, password=None, pair='L', size=7.5, preference="M", **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, pair, size, preference, **extra_fields)
