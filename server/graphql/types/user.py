"""User GraphQL types."""
import graphene 
from authentication.models import User as UserModel
from .location import Location as LocationType

from graphene_django import DjangoObjectType


class User(DjangoObjectType):
    """GraphQL type for the User model."""

    location = graphene.Field(LocationType)

    class Meta:
        model = UserModel
        only_fields = ("email", "password", "clothing_preference", "pair", "size", "location", "distance")

    def resolve_email(self, info, **kwargs):
        """Keep email private except if you're the current user."""
        if info.context.user == self:
            return self.email
        return ""

    def resolve_password(self, info, **kwargs):
        return self.password

    def resolve_clothing_preference(self, info, **kwargs):
        return self.clothing_preference
        
    def resolve_pair(self, info, **kwargs):
        return self.pair

    def resolve_size(self, info, **kwargs):
        return self.size
    
    def resolve_location(self, info, **kwargs):
        return self.location

    def distance(self, info, **kwargs):
        return getattr(self, 'distance', None)