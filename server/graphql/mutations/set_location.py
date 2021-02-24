import graphene
from django.contrib.auth import authenticate, login
from django.contrib.gis.geos import Point

from authentication.models import LocationData, User
from ..types.location import Location as LocationType


class SetLocation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        address = graphene.String()
        city = graphene.String()
        state = graphene.String()
        latitude = graphene.Float()
        longitude = graphene.Float()

    def mutate(self, info, address, latitude, longitude, city, state, **kwargs):

        user = User.objects.get(id=info.context.user.id)

        point = Point(longitude, latitude, srid=4326)
        print(point)

        if user.location == None:
            location = LocationData(
                address=address, latitude=latitude, longitude=longitude, city=city, state=state, point=point)
            location.save()
            user.location = location
            user.save()

        else:
            user.location.point = point
            user.location.address = address
            user.location.city = city
            user.location.adress = state
            user.location.latitude = latitude
            user.location.longitude = longitude
            user.location.save()

        return SetLocation(location=user.location)
