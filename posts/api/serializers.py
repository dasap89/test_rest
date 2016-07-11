from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    )

from posts.models import Post
from accounts.api.serializers import UserDetailSerializer


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]

class PostDetailSerializer(ModelSerializer):
    # user = SerializerMethodField()
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user',
            'image',
            'title',
            'slug',
            'content',
            'publish',
            'markdown',
        ]
    
    def get_markdown(self, obj):
        return obj.get_markdown()
    
    # def get_user(self, obj):
    #     return str(obj.user.username)
    
    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug',
        )
    # user = SerializerMethodField()
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'user',
            'slug',
            'content',
            'publish',
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)