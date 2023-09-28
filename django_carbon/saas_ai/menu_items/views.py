# from django.shortcuts import render
# from django.contrib.auth.models import User, Group
# from menu_items.serializers import *
# from rest_framework import viewsets
# from rest_framework import mixins,generics,status
# # Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
from .models import *
from .serializers import *
from rest_framework.permissions import (AllowAny)
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import os
from django.http import Http404
# import request
from django.conf import settings
from rest_framework import status, generics, mixins
import re
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist

# class SingerViewSet(viewsets.ModelViewSet):
#     queryset=Singer.objects.all()
#     serializer_class=SingerSerializer

# class SongViewSet(viewsets.ModelViewSet):
#     queryset=Song.objects.all()
#     serializer_class=SongSerializer



class CarbonTableAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = CarbonTable.objects.all().order_by('id')
    serializer_class = CarbonTableSerializer

    def get_object(self, id):
        try:

            return CarbonTable.objects.get(id=id)
        except CarbonTable.DoesNotExist:
            raise Http404

    def get(self, request,id=None, *args, **kwargs):
        if id:
            id_obj = self.get_object(id)
            serializer = CarbonTableSerializer(id_obj)
            return Response(serializer.data)
        else:
            alldata = CarbonTable.objects.all()
            serializer = CarbonTableSerializer(alldata, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CarbonTableSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,id=None, *args, **kwargs):
        agent_type = self.get_object(id)
        serializer = CarbonTableSerializer(agent_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # data = serializer.data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            CarbonTable.objects.filter(id=id).delete()
            message = {"success": "sucessfully deleted"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)



class CarbonInputAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = Carbon.objects.all().order_by('id')
    serializer_class = CarbonInputSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    def get_object(self, id):
        try:

            return Carbon.objects.get(id=id)
        except Carbon.DoesNotExist:
            raise Http404

    def get(self, request,id=None, *args, **kwargs):
        if id:
            id_obj = self.get_object(id)
            serializer = CarbonInputSerializer(id_obj)
            return Response(serializer.data)
        else:
            alldata = Carbon.objects.all()
            serializer = CarbonInputSerializer(alldata, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CarbonInputSerializer(data=data,many=True)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,id=None, *args, **kwargs):
        agent_type = self.get_object(id)
        serializer = CarbonInputSerializer(agent_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # data = serializer.data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            Carbon.objects.filter(id=id).delete()
            message = {"success": "sucessfully deleted"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)





class CarbonAPIView(generics.GenericAPIView,mixins.ListModelMixin):

    queryset = Carbon.objects.all().order_by('-id')[:7]
    serializer_class = CarbonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get_object(self, id):
    #     try:

    #         return Carbon.objects.get(id=id)
    #     except CarbonSerializer.DoesNotExist:
    #         raise Http404

    # def get(self, request,id=None, *args, **kwargs):
    #     if id:
    #         id_obj = self.get_object(id)
    #         serializer = CarbonSerializer(id_obj)
    #         return Response(serializer.data)
    #     else:
    #         alldata = Carbon.objects.all()
    #         serializer = CarbonSerializer(alldata, many=True)
    #         return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = CarbonSerializer(data=data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.aaa=(serializer.aaa)* (serializer.q)
    #         data = serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request,id=None, *args, **kwargs):
    #     agent_type = self.get_object(id)
    #     serializer = CarbonSerializer(agent_type, data=request.data, partial=True)
    #     if serializer.is_valid():
            
    #         serializer.save()
    #         # data = serializer.data
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, id=None, *args, **kwargs):
    #     try:
    #         Carbon.objects.filter(id=id).delete()
    #         message = {"success": "sucessfully deleted"}
    #         return Response(message, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         error = getattr(e, 'message', repr(e))
    #         return Response(error, status=status.HTTP_400_BAD_REQUEST)




class StructuralElementAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = StructuralElement.objects.all().order_by('id')
    serializer_class = StructuralElementSerializer

    def get_object(self, id):
        try:

            return StructuralElement.objects.get(id=id)
        except StructuralElement.DoesNotExist:
            raise Http404

    def get(self, request,id=None, *args, **kwargs):
        if id:
            id_obj = self.get_object(id)
            serializer = StructuralElementSerializer(id_obj)
            return Response(serializer.data)
        else:
            alldata = StructuralElement.objects.all()
            serializer = StructuralElementSerializer(alldata, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StructuralElementSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,id=None, *args, **kwargs):
        agent_type = self.get_object(id)
        serializer = StructuralElementSerializer(agent_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # data = serializer.data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            StructuralElement.objects.filter(id=id).delete()
            message = {"success": "sucessfully deleted"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)



class ElementGroupAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = ElementGroup.objects.all().order_by('id')
    serializer_class = ElementGroupSerializer

    def get_object(self, id):
        try:

            return ElementGroup.objects.get(id=id)
        except ElementGroup.DoesNotExist:
            raise Http404

    def get(self, request,id=None, *args, **kwargs):
        if id:
            id_obj = self.get_object(id)
            serializer = ElementGroupSerializer(id_obj)
            return Response(serializer.data)
        else:
            alldata = ElementGroup.objects.all()
            serializer = ElementGroupSerializer(alldata, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ElementGroupSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,id=None, *args, **kwargs):
        agent_type = self.get_object(id)
        serializer = ElementGroupSerializer(agent_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # data = serializer.data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            ElementGroup.objects.filter(id=id).delete()
            message = {"success": "sucessfully deleted"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)



















#############################################################################################################

# class CarbonReferenceAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

#     queryset = CarbonReference.objects.all().order_by('id')
#     serializer_class = CarbonReferenceSerializer

#     def get_object(self, id):
#         try:

#             return CarbonReference.objects.get(id=id)
#         except CarbonReferenceSerializer.DoesNotExist:
#             raise Http404

#     def get(self, request,id=None, *args, **kwargs):
#         if id:
#             id_obj = self.get_object(id)
#             serializer = CarbonReferenceSerializer(id_obj)
#             return Response(serializer.data)
#         else:
#             alldata = CarbonReference.objects.all()
#             serializer = CarbonReferenceSerializer(alldata, many=True)
#             return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = CarbonReferenceSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             data=serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request,id=None, *args, **kwargs):
#         agent_type = self.get_object(id)
#         serializer = CarbonReferenceSerializer(agent_type, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             # body_data = serializer.data
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id=None, *args, **kwargs):
#         try:
#             CarbonReference.objects.filter(id=id).delete()
#             message = {"success": "sucessfully deleted"}
#             return Response(message, status=status.HTTP_200_OK)
#         except Exception as e:
#             error = getattr(e, 'message', repr(e))
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)


# class InputTableAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

#     queryset = InputTable.objects.all().order_by('id')
#     serializer_class = InputTableSerializer

#     def get_object(self, id):
#         try:

#             return InputTable.objects.get(id=id)
#         except InputTableSerializer.DoesNotExist:
#             raise Http404

#     def get(self, request,id=None, *args, **kwargs):
#         if id:
#             id_obj = self.get_object(id)
#             serializer = InputTableSerializer(id_obj)
#             return Response(serializer.data)
#         else:
#             alldata = InputTable.objects.all()
#             serializer = InputTableSerializer(alldata, many=True)
#             return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = InputTableSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             data = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request,id=None, *args, **kwargs):
#         agent_type = self.get_object(id)
#         serializer = InputTableSerializer(agent_type, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             # body_data = serializer.data
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id=None, *args, **kwargs):
#         try:
#             InputTable.objects.filter(id=id).delete()
#             message = {"success": "sucessfully deleted"}
#             return Response(message, status=status.HTTP_200_OK)
#         except Exception as e:
#             error = getattr(e, 'message', repr(e))
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)


# ###########################################################################

# class SongAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

#     queryset = Song.objects.all().order_by('id')
#     serializer_class = SongSerializer

#     def get_object(self, id):
#         try:

#             return Song.objects.get(id=id)
#         except SongSerializer.DoesNotExist:
#             raise Http404

#     def get(self, request,id=None, *args, **kwargs):
#         if id:
#             id_obj = self.get_object(id)
#             serializer = SongSerializer(id_obj)
#             return Response(serializer.data)
#         else:
#             alldata = Song.objects.all()
#             serializer = SongSerializer(alldata, many=True)
#             return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = SongSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             data = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request,id=None, *args, **kwargs):
#         agent_type = self.get_object(id)
#         serializer = SongSerializer(agent_type, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             # body_data = serializer.data
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id=None, *args, **kwargs):
#         try:
#             Song.objects.filter(id=id).delete()
#             message = {"success": "sucessfully deleted"}
#             return Response(message, status=status.HTTP_200_OK)
#         except Exception as e:
#             error = getattr(e, 'message', repr(e))
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)





# class SingerAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

#     queryset = Singer.objects.all().order_by('id')
#     serializer_class = SingerSerializer

#     def get_object(self, id):
#         try:

#             return Singer.objects.get(id=id)
#         except SingerSerializer.DoesNotExist:
#             raise Http404

#     def get(self, request,id=None, *args, **kwargs):
#         if id:
#             id_obj = self.get_object(id)
#             serializer = SingerSerializer(id_obj)
#             return Response(serializer.data)
#         else:
#             alldata = Singer.objects.all()
#             serializer = SingerSerializer(alldata, many=True)
#             return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = SingerSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             data = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request,id=None, *args, **kwargs):
#         agent_type = self.get_object(id)
#         serializer = SingerSerializer(agent_type, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             # body_data = serializer.data
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id=None, *args, **kwargs):
#         try:
#             Singer.objects.filter(id=id).delete()
#             message = {"success": "sucessfully deleted"}
#             return Response(message, status=status.HTTP_200_OK)
#         except Exception as e:
#             error = getattr(e, 'message', repr(e))
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)


# class ItemAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

#     queryset = Item.objects.all().order_by('id')
#     serializer_class = ItemSerializer

#     def get_object(self, id):
#         try:

#             return Item.objects.get(id=id)
#         except ItemSerializer.DoesNotExist:
#             raise Http404

#     def get(self, request,id=None, *args, **kwargs):
#         if id:
#             id_obj = self.get_object(id)
#             serializer = ItemSerializer(id_obj)
#             return Response(serializer.data)
#         else:
#             alldata = Item.objects.all()
#             serializer = ItemSerializer(alldata, many=True)
#             return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = ItemSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             data = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request,id=None, *args, **kwargs):
#         agent_type = self.get_object(id)
#         serializer = ItemSerializer(agent_type, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             # body_data = serializer.data
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id=None, *args, **kwargs):
#         try:
#             Item.objects.filter(id=id).delete()
#             message = {"success": "sucessfully deleted"}
#             return Response(message, status=status.HTTP_200_OK)
#         except Exception as e:
#             error = getattr(e, 'message', repr(e))
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)