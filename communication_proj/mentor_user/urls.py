from django.urls import path, include
from .views import Registeruser, UserMessageAPI, MenterMessageAPI, MenterListAPI, MenterMessageReplayAPI

urlpatterns = [
    path('user/', Registeruser.as_view(),name='create_or_get_users'),
    path('user/<int:user_id>/message/', UserMessageAPI.as_view(),name='create_or_list_msg'),
    path('menter/', MenterListAPI.as_view(),name='list_all_mentors'),
    path('mentor/<int:mentor_id>/message/', MenterMessageAPI.as_view(),name='list_mentor_msgs'),
    path('mentor/<int:mentor_id>/message/<int:message_id>/', MenterMessageReplayAPI.as_view(),name='list_mentor_msgs'),
    path('mentor/<int:mentor_id>/message/<int:message_id>/', MenterMessageReplayAPI.as_view(),name='list_mentor_msgs'),
    # path('user/<int:user_id>/Request', MenterRequestForAccepting.as_view(),name='request_for_mentor_acceptance')
]