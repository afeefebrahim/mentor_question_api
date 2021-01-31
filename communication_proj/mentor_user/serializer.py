from rest_framework import serializers
from .models import UserProfile, MenterRequest, Replay, Message
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User

# create class to serializer usermodel
class UserProfileSerializer(serializers.ModelSerializer):  
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = UserProfile
        fields = ('email', 'username', 'first_name', 'last_name', 'password')
        # fields = ()



class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('heading', 'content', 'attach', 'sender')


class MentorProfileSerializer(UserProfileSerializer):

    class Meta:
        model = UserProfile
        fields = ('id','email', 'username', 'first_name', 'last_name', )



class MentorMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'heading', 'content', 'attach', 'sender_id')


class MenterMessageReplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay
        fields = ('replay_text',)
