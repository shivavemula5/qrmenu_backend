from django.db.models import Q

from rest_framework.viewsets import ModelViewSet

from core.models import Place , Category , MenuItem
from core.api.serializers import PlaceSerializer , PlaceDetailSerializer , CategorySerializer , MenuItemSerializer
from core.api.permissions import AuthorPlaceOrReadOnly , AuthorPlaceCatogoryOrReadOnly 

class PlaceViewSet(ModelViewSet):
    
    serializer_class = PlaceSerializer
    permission_classes = [AuthorPlaceOrReadOnly]

    def get_queryset(self):
        queryset = Place.objects.filter()  
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class PlaceDetailViewSet(ModelViewSet):
    
    serializer_class = PlaceDetailSerializer
    permission_classes = [AuthorPlaceOrReadOnly]
    
    def get_queryset(self):
        queryset = Place.objects.filter(owner_id=self.request.user.id)  
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryViewSet(ModelViewSet):
    
    serializer_class = CategorySerializer
    permission_classes = [AuthorPlaceCatogoryOrReadOnly]
    
    def get_queryset(self):
        queryset = Category.objects.filter(place_id=self.kwargs['place_pk'])
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(place_id= self.kwargs['place_pk'])

class MenuItemViewSet(ModelViewSet):
    
    serializer_class = MenuItemSerializer
    permission_classes = [AuthorPlaceCatogoryOrReadOnly]
    
    def get_queryset(self):
        queryset = MenuItem.objects.filter(Q(place_id=self.kwargs['place_pk']) & Q(category_id=self.kwargs['categories_pk']))
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(place_id=self.kwargs['place_pk'],category_id=self.kwargs['categories_pk'])
