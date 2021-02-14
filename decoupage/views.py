from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Region
from .serializers import RegionSerializer


class RegionListView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetailView(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionViewSet(ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
