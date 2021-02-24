from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="donations", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    claimed = models.BooleanField(default=False)
    claimant = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, default=None, on_delete=models.SET_NULL)

    MASCULINE = "M"
    FEMININE = "F"
    A = "A"

    PREFRENCE_OPTIONS = [(MASCULINE, "Male presenting clothing"), (
        FEMININE, "Female presenting clothing"), (A, "Any")]

    size = models.FloatField(_('size'))

    clothing_type = models.CharField(
        _("clothing type"), choices=PREFRENCE_OPTIONS, default=A, max_length=1)


class Tag(models.Model):
    tag = models.CharField(null=False, max_length=50)
    item = models.ForeignKey(Item, related_name="tags",
                             on_delete=models.CASCADE)
