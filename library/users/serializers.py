from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User, Profile


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                 'email',
                 'first_name',
                 'last_name',
                 ]


class ProfileModelSerializer(HyperlinkedModelSerializer):
    user = UserModelSerializer()
    class Meta:
        model = Profile
        fields = '__all__'
