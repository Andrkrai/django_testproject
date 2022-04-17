# serializers.py
from rest_framework import serializers
from catalog.models import Category, Product
from feedbacks.models import Feedback


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'slug')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'slug', 'category')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'full_name', 'email', 'phone', 'product', 'description', 'grade')
