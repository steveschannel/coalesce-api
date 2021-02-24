import graphene
from django.contrib.auth import authenticate, login
from django.contrib.gis.geos import Point

from sharing.models import Item
from authentication.models import User
from ..types.item import Item as ItemType


class CreateItem(graphene.Mutation):
    item = graphene.Field(ItemType)

    class Arguments:
        size = graphene.Float()
        title = graphene.String()
        clothing_type = graphene.String()

    def mutate(self, info, size, title, clothing_type, **kwargs):

        user = User.objects.get(id=info.context.user.id)

        item = Item(
            size=size, title=title, user=user, clothing_type=clothing_type)
        item.save()

        return CreateItem(item=item)
