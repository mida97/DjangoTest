from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = User
       fields = ['username',
                 'email',
                 'first_name',
                 'last_name',
                 ]

'''
def update(self, instance):
   instance.set_password(raw_password='init123')
   instance.save()

   return instance
'''
