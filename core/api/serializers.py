from rest_framework import serializers
from core.models import Place , Category , MenuItem

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id','name','image','number_of_tables']
        read_only_fields = ['id']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','place','category','name','description','price','image','is_available']
        read_only_fields = ['id']

class CategorySerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','place','name','menuitem']
        read_only_fields = ['id']


class PlaceDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True,read_only=True) 
    class Meta:
        model = Place   
        fields = ['id','name','image','number_of_tables','category']
    
