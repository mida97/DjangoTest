from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
#from rest_framework import filters
from .models import Project
from .serializers import ProjectModelSerializer
from django_filters import rest_framework as filters
from rest_framework.decorators import api_view, renderer_classes


class PrFilter(filters.FilterSet):
   name = filters.CharFilter(lookup_expr='contains')
   change_date = filters.DateFilter(lookup_expr='lte')
   change_date_time = filters.DateFilter(field_name='change_date_time', lookup_expr='date')

   class Meta:
       model = Project
       fields = ['name', 'change_date', 'change_date_time']


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = PrFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activate_project()
        return Response(status=status.HTTP_204_NO_CONTENT)
