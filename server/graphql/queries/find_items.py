from sharing.models import Item
from sharing.models import Tag
from authentication.models import User
from authentication.models import LocationData

def FindItems(usr):
    user = User.objects.get(pk=usr.id)


    



