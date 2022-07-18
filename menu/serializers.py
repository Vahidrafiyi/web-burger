from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import *


class MenuItemSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    class Meta:
        model = MenuItem
        fields = ['id', 'menu_item_title', 'menu_item_order', 'category']


class MenuCategorySerializer(serializers.ModelSerializer):
    # menuitem = MenuItemSerializer(read_only=True, many=True)
    class Meta:
        model = MenuCategory
        fields = '__all__'

    # def create(self, validated_data):
    #     menuitems = validated_data.pop('tracks')
    #     category = MenuCategory.objects.create(**validated_data)
    #     for menuitem in menuitems:
    #         MenuItem.objects.create(category=category, **menuitem)
    #     return category


class MenuSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Menu
        fields = ('id', 'name', 'parent', 'children')
