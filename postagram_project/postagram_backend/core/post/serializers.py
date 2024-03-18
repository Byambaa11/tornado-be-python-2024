from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.post.models import Post
from core.user.models import User

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='public_id')
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for anotheruser.")
        return value
    class Meta:
        model = Post
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields = ["edited"]
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author, context=self.context).data
        return rep
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
            
        instance = super().update(instance, validated_data)
        
        return instance
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'edited', 'liked',  'likes_count', 'comments_count', 'created', 'updated']
        
        read_only_fields = ["edited"]
        