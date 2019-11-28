from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
# Create your views here.

from .models import PileColor, HedgeHog, Comment
from .serializers import UserSerializer, PileColorSerializer, HedgeHogSerializer,CommentSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all().order_by('first_name')
    serializers_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PileColorListCreate(generics.ListCreateAPIView):
    """ List and create PileColors """
    queryset = PileColor.objects.all()
    serializer_class = PileColorSerializer
    permission_classes = (permissions.IsAuthenticated, )


class PileColorRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update PileColor information """
    queryset = PileColor.objects.all()
    serializer_class = PileColorSerializer
    permission_classes = (permissions.IsAuthenticated, )


class HedgeHogListCreate(generics.ListCreateAPIView):
    """List and create HedgeHogs """
    queryset = HedgeHog.objects.all().order_by('name')
    serializer_class = HedgeHogSerializer
    permission_classes = (permissions.IsAuthenticated, )


class HedgeHogRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Retrieve and update a HedgeHog"""
    queryset = HedgeHog.objects.all()
    serializer_class = HedgeHogSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentListCreate(generics.ListCreateAPIView):
    """ List or create a HedgeHog """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ List or create a HedgeHog """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )