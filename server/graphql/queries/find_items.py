import graphene

from authentication.models import User
from django.db.models import Q
from ..types.user import User as UserType

from sharing.models import Item
from ..types.item import Item as ItemType

from authentication.models import LocationData
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from django.contrib.gis.measure import D 
from django.db.models import OuterRef, Subquery

def FindItems(usr):
    user = User.objects.get(pk=usr.id)

    user_location = user.location.point

    users = User.objects.filter(donations__isnull=False).exclude(pk=user.id).distinct().annotate(distance=Subquery(LocationData.objects.filter(pk=OuterRef('pk')).annotate(distance=Distance('point', user_location)).values('distance'))).order_by('distance')

    return users





