# from rest_framework import routers
from menu_items.views import *

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

from django.urls import include, path
# from rest_framework import routers
from menu_items import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

from django.urls import path,include
from .views import *
from django.conf.urls import *


urlpatterns=[

    path('carbon_input/', CarbonInputAPIView.as_view(),name='carbon_input_list'),
    path('carbon_input/<int:id>/', CarbonInputAPIView.as_view(),name='carbon_input_operation'),

    path('carbon/', CarbonAPIView.as_view(),name='carbon_list'),
    path('carbon/<int:id>/', CarbonAPIView.as_view(),name='carbon_operation'),

    path('carbon_table/', CarbonTableAPIView.as_view(),name='carbon_table_list'),
    path('carbon_table/<int:id>/', CarbonTableAPIView.as_view(),name='carbon_table_operation'),

    path('structural/', StructuralElementAPIView.as_view(),name='structural_list'),
    path('structural/<int:id>/',StructuralElementAPIView.as_view(),name='structural_operation'),

    path('element/', ElementGroupAPIView.as_view(),name='element_list'),
    path('element/<int:id>/', ElementGroupAPIView.as_view(),name='element_operation'),



    # path('carbon_reference/', CarbonReferenceAPIView.as_view(),name='carbon_reference_list'),
    # path('carbon_reference/<int:id>/', CarbonReferenceAPIView.as_view(),name='carbon_reference_operation'),

    # path('input_table/', InputTableAPIView.as_view(),name='input_table_list'),
    # path('input_table/<int:id>/', InputTableAPIView.as_view(),name='input_table_operation'),

    # path('song/', SongAPIView.as_view(),name='song_list'),
    # path('song/<int:id>/', InputTableAPIView.as_view(),name='song_operation'),

    # path('singer/', SingerAPIView.as_view(),name='singer_list'),
    # path('singer/<int:id>/', InputTableAPIView.as_view(),name='singer_operation'),

    # path('item/', ItemAPIView.as_view(),name='item_list'),
    # path('item/<int:id>/', ItemAPIView.as_view(),name='item_operation'),

]
    