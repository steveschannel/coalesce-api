"""User GraphQL types."""
import graphene 
from sharing.models import Item as ItemModel

from graphene_django import DjangoObjectType


class Item(DjangoObjectType):
    class Meta:
        model = ItemModel
        only_fields = ("title", "claimant")

    def resolve_title(self, info, **kwargs):
        return self.title

    def resolve_claimant(self, info, **kwargs):
        return self.claimant
