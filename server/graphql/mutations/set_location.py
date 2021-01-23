import graphene
from django.contrib.auth import authenticate, login

from authentication.models import LocationData, User
from ..types.location import Location as LocationType


class SetLocation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        address = graphene.String()
        city = graphene.String()
        state = graphene.String()
        latitude = graphene.Decimal()
        longitude = graphene.Decimal()

    def mutate(self, info, address, latitude, longitude, city, state, **kwargs):

        user = User.objects.get(id=info.context.user.id)

        if user.location == None:
            location = LocationData(address=address, latitude=latitude, longitude=longitude, city=city, state=state)
            location.save()
            user.location = location
            user.save()

        else:
            user.location.adress = address
            user.location.city = city
            user.location.adress = state
            user.location.latitude = latitude
            user.location.longitude = longitude

        return SetLocation(location=user.location)
