from .models import Author, Post, Category
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['rating', ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'post_type', 'created', 'cats', 'title', 'text', 'rating' ]
