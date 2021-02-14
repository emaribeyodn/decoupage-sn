from django.urls import path, include
from rest_framework import routers
from .views import RegionDetailView, RegionListView, RegionViewSet


router = routers.DefaultRouter()
router.register('regions', RegionViewSet)

urlpatterns = [
    # path("regions/", RegionListView.as_view(), name="region_list"),
    # path("regions/<pk>", RegionDetailView.as_view(), name="region_detail"),
    path('', include(router.urls))
]
