"""Main GraphQL schema file. Only one for this project."""
from .graphql.types.user import User as UserType
from .graphql.types.location import Location as LocationType
from .graphql.types.item import Item as ItemType
from .graphql.mutations.logout_user import LogoutUser
from .graphql.queries.find_items import FindItems
from .graphql.mutations.set_location import SetLocation
from .graphql.mutations.login_user import LoginUser
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    me = graphene.Field(UserType)

    find_items = graphene.List(ItemType)

    def resolve_me(self, info, **kwargs):
        """Return the current logged in user."""
        return info.context.user

    def resolve_find_items(self, info, **kwargs):
        return FindItems(info.context.user, info, **kwargs)

class Mutation(graphene.ObjectType):

    logout_user = LogoutUser.Field(description="Log the user out.")
    login_user = LoginUser.Field(description="Login.")
    set_location = SetLocation.Field(description="Set user location")
    # post_item = PostItem.Field(description="Set user location")
    # claim_item = ClaimItem.Field(description="Set user location")
    # remove_item = RemoveItem.Field(description="Set user location")

schema = graphene.Schema(query=Query, mutation=Mutation)
