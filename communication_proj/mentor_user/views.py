from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render
from .serializer import UserProfileSerializer, MessageSerializer, MentorProfileSerializer, MentorMessageSerializer, MenterMessageReplaySerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView
from .models import UserProfile, Message, Replay
from .pagination import CustomPagination
from .permission import IsOwnerOrReadOnly, IsAuthenticated

# Create your views here.



class Registeruser(CreateAPIView):
    serializer_class = UserProfileSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    # paginator = 
    def get_queryset(self):
       users = UserProfile.objects.all()
       return users

    # Get all users
    def get(self, request):
        users = self.get_queryset()
        paginate_queryset = self.paginate_queryset(users)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)
        # import ipdb; ipdb.set_trace()
        # return users

    # Create a new suer
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMessageAPI(ListCreateAPIView):
    serializer_class = MessageSerializer
    # lookup_field = 'user_id'
    permission_classes = (IsAuthenticated,)
    # lookup_url_kwarg = 'user_id'

    def get_queryset(self):
        queryset = Message.objects.filter(sender_id=self.kwargs.get('user_id'))
        return queryset

    # Create a query
    def perform_create(self, serializer):
        # import ipdb; ipdb.set_trace()
        serializer.save(sender_id=self.kwargs.get('user_id'))


class MenterListAPI(ListAPIView):
    serializer_class = MentorProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = UserProfile.objects.filter(is_mentor=True)
        return queryset

    # Create a query
    # def perform_create(self, serializer):
    #     # import ipdb; ipdb.set_trace()
    #     serializer.save(sender_id=self.kwargs.get('user_id'))

# class MenterListAPI(RetrieveAPIView):
#     lookup_field = 'id'
#     serializer_class = MentorProfileSerializer

    # def get_queryset(self):
    #     queryset = UserProfile.objects.filter(id)
    #     return queryset


class MenterMessageAPI(ListAPIView):
    serializer_class = MentorMessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Message.objects.filter(msg_send_to_mentor=self.kwargs.get('mentor_id'))
        return queryset

    # Create a query
    def perform_create(self, serializer):
        # import ipdb; ipdb.set_trace()
        serializer.save(sender_id=self.kwargs.get('user_id'))



class MenterMessageReplayAPI(ListAPIView):
    serializer_class = MentorMessageSerializer
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     queryset = Message.objects.filter(msg_send_to_mentor=self.kwargs.get('mentor_id'))
    #     return queryset

    # Create a query
    def perform_create(self, serializer):
        # import ipdb; ipdb.set_trace()
        serializer.save(sender_id=self.kwargs.get('user_id'))
    


class MenterMessageReplayAPI(ListCreateAPIView):
    serializer_class = MenterMessageReplaySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Replay.objects.filter(message_id=self.kwargs.get('message_id'))
    #     queryset = Message.objects.filter(msg_send_to_mentor=self.kwargs.get('mentor_id'))


    def perform_create(self, serializer):
        serializer.save(replayed_by_id=self.kwargs.get('mentor_id'), message_id= self.kwargs.get('message_id'))


# class MenterRequestForAcceptAPI(CreateAPIView):
#     serializer_class = MenterRequestForAcceptSerializer

#     def perform_create(self, serializer):
#         serializer.save(requested_from_id=self.kwargs.get('mentor_id'))