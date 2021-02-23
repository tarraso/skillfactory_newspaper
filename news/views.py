from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from news.serializers import AuthorSerializer
from news.models import Author, Post


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by("-rating")
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-rating")
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
