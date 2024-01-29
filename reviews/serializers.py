from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from .models import Product,Category,Company,ProductSite,Comment,ProductSize,Image
from django.contrib.auth.models import User
from django.utils.timezone import now
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes = 'product_headshot'
        # sizes= [
        #     # ('full_size','url'),
        #     # ('thumbnail','thumbnail__100x100')
        # ]
    )
    class Meta:
        model = Image
        fields = ['pk','name','image']

class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk','name']

class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk','name']
        expandable_fields = {
            'products': ('reviews.ProductSerializer',{'many':True})
        }
     
class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']
  
class ProductSerializer(FlexFieldsModelSerializer):
    # category = CategorySerializer(many=True)
    class Meta:
        model = Product
        # fields = ['pk', 'name', 'category']
        fields = ['pk', 'name', 'content','created','updated']
        read_only_fields = ['pk']
        expandable_fields = {
            'category': (CategorySerializer,{'many':True}),
            'sites': ('reviews.ProductSiteSerializer',{'many':True}),
            'comments': ('reviews.CommentSerializer',{'many':True}),
            'image': ('reviews.ImageSerializer',{'many':True}),
        }

class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'created', 'updated']
        expandable_fields = {
            'product': 'reviews.CategorySerializer',
            'productsize': 'reviews.ProductSizeSerializer',
            'company': 'reviews.CompanySerializer',
        }

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
    
    def get_days_since_joined(self,obj):
        return (now() - obj.date_joined).days

class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'reviews.CategorySerializer',
            'user': 'reviews.UserSerializer'
        }




