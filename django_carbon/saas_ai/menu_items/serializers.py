# from rest_framework import serializers
# from django.contrib.auth.models import User,Group

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

from rest_framework import serializers
from .models import *






# class CarbonReferenceSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = CarbonReference
#         fields= '__all__'


class ElementGroupSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ElementGroup
        fields= '__all__'
        # depth = 1

class StructuralElementSerializer(serializers.ModelSerializer):
    class Meta: 
        model = StructuralElement
        fields= '__all__'
        # depth = 1
class CarbonTableSerializer(serializers.ModelSerializer):
    
    # carbon=serializers.SlugRelatedField(many=True,read_only=True,slug_field=CarbonTable.a1_a3)
    # carbon=CarbonSerializer(many=True)
    # def create(self, validated_data):
    #     songs_data = validated_data.pop("carbon")
    #     func1 = CarbonTable.objects.create(**validated_data)
    #     for song_data in songs_data:
    #         Carbon.objects.create(func1=func1)
    #     return func1

    class Meta: 
        model = CarbonTable
        fields= ('material_specification','a1_a3','a4','wf','c2','c3_c4','c2_c4','d','total_a1_a5','total_a_c')
#    order = serializers.PrimaryKeyRelatedField(read_only=True)
#     price = serializers.ReadOnlyField()
#    price = serializers.IntegerField()



class CarbonInputSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Carbon
        fields =('id','carbon_table','substructural_element','element_group','gia','quantity')


class CarbonSerializer(serializers.ModelSerializer):
    # c1=Carbon.objects.get(id)
    # c2=c1.A1_A3
    # c2=serializers.ReadOnlyField()
    # carbon=Carbon.objects.all()
    carbon_name = serializers.CharField(source='carbon_table.material_specification')
    substructural_element_name = serializers.CharField(source='substructural_element.element_name')
    element_group_name = serializers.CharField(source='element_group.group_name')
    q=serializers.IntegerField(source='quantity')
    A1_A3 = serializers.IntegerField()
    A4 = serializers.IntegerField()
    A5w = serializers.IntegerField()
    C2 = serializers.IntegerField()
    C3_C4 = serializers.IntegerField()
    C2_C4 = serializers.IntegerField()
    D = serializers.IntegerField()
    TOTAL_A1_A5 = serializers.IntegerField()
    TOTAL_A_C = serializers.IntegerField()
    A_C_m2 = serializers.IntegerField()
    A1_A5_m2 = serializers.IntegerField()

    # aaa2=serializers.CharField(source='carbon.A1_A3')
    # carbon=CarbonTableSerializer(read_only=True,many=True)
    # func1=serializers.ReadOnlyField()
    # album_musician=ElementGroupSerializer(read_only=True, many=True)
    # structure=StructuralElementSerializer(read_only=True, many=True)
    # a1a3=serializers.CharField(source='A1_A3')
    class Meta: 
        model = Carbon
        fields =('carbon_name','substructural_element_name','element_group_name','gia','q','A1_A3','A4','A5w','C2','C3_C4','C2_C4','D','TOTAL_A1_A5','TOTAL_A_C','A_C_m2','A1_A5_m2')











#################################################################################################################        
# 'func1'

        # depth = 1

# class InputTableSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = InputTable
#         fields= '__all__'



# class SongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Song
#         fields=['id','title','singer','duration']

# class SingerSerializer(serializers.ModelSerializer):
#     song=serializers.StringRelatedField(many=True,read_only=True)
#     class Meta:
#         model=Singer
#         fields=['id','name','gender','song']

# class CategorySerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=Category
#         fields='__all__'


# class ItemSerializer(serializers.ModelSerializer):
#     category_name = serializers.CharField(source='category.name',read_only=True)

#     class Meta:
#         model = Item
#         fields = ('id', 'name', 'category_name')









#         fields= ('id','carbon_table','substructural_element','element_group','gia','quantity','structure','album_musician')
    
#     def create(self, validated_data):
#         albums_data = validated_data.pop('album_musician')
#         musician = Carbon.objects.create(**validated_data)
#         for album_data in albums_data:
#             ElementGroup.objects.create(artist=musician, **album_data)
#         return musician

#     def update(self, instance, validated_data):
#         albums_data = validated_data.pop('album_musician')
#         albums = (instance.album_musician).all()
#         albums = list(albums)
#         instance.carbon_table = validated_data.get('carbon_table', instance.carbon_table)
#         instance.substructural_element = validated_data.get('substructural_element', instance.substructural_element)
#         instance.element_group = validated_data.get('element_group', instance.element_group)
#         instance.gia = validated_data.get('gia', instance.gia)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.instrument = validated_data.get('instrument', instance.instrument)
#         instance.save()

#         for album_data in albums_data:
#             album = albums.pop(0)
#             album.element_group = album_data.get('element_group', album.element_group)
#             album.save()
#         return instance
# # album_musician = AlbumSerializer(read_only=True, many=True)