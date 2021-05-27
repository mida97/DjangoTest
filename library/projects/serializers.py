from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        #exclude = [  "change_date",]
        fields = '__all__'
