
from authentication.models import LocationData as LocationModel
from graphene_django import DjangoObjectType


class Location(DjangoObjectType):

    class Meta:
        model = LocationModel

    def resolve_address(self, info, **kwargs):
        return self.address

    def resolve_latitute(self, info, **kwargs):
        return self.latitude

    def resolve_longitude(self, info, **kwargs):
        return self.longitude 
    
    def resolve_city(self, info, **kwargs):
        return self.city
    
    def resolve_state(self, info, **kwargs):
        return self.state