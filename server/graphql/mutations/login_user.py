import graphene
from django.contrib.auth import authenticate, login

from ..types.user import User as UserType


class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, email, password, **kwargs):

        user = authenticate(email=email, password=password)
        login(info.context, user)

        return LoginUser(user=user)
