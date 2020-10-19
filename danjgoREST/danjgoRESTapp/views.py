from django.shortcuts import render

from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions

from danjgoREST.danjgoRESTapp.serializers import UserSerializer, GroupSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    #Allows users to be viewed or edited
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    #Allows groups to be viewed or edited
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]