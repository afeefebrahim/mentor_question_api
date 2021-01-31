from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


# class User(AbstractUser):
#     is_mentee = models.BooleanField(default=False)
#     is_mentor = models.BooleanField(default=False)


class UserProfile(User): 
  # username = models.CharField(max_length = 50, blank = True, null = True, unique = True) 
  # email = models.EmailField(unique = True) 
  # first_name = models.CharField(max_length = 50)
  # last_name = models.CharField(max_length = 50) 
  phone_no = models.CharField(max_length = 12) 
  is_mentor = models.BooleanField(default=False)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] 
  def __str__(self): 
      return "{}".format(self.email)


# class Mentor(AbstractUser):
    # pass 
  # username = models.CharField(max_length = 50, blank = True, null = True, unique = True) 
  # email = models.EmailField(unique = True) 
  # # first_name = models.CharField(max_length = 50)
  # # last_name = models.CharField(max_length = 50) 
  # phone_no = models.CharField(max_length = 12) 
  # USERNAME_FIELD = 'email'
  # REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] 
  # def __str__(self): 
  #     return "{}".format(self.email) 

class MenterRequest(models.Model):
    requested_to = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='mentor_request')
    requested_from = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_request')
    is_accepted = models.BooleanField(default=False)
    is_request_exits = models.BooleanField(default=True)
    request_time = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        self.is_request_exits = True
        super().save()


class Message(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=500, blank=True)
    attach = models.FileField(upload_to ='uploads/% Y/% m/% d/',  blank=True)
    sender = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='user')
    msg_send_to_mentor = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='msg_send_mentor')
    created_on = models.DateTimeField(auto_now=True)

class Replay(models.Model):
    replay_text = models.TextField(max_length=500, blank=True)
    replayed_by = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='mentor')
    user_comment = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    message = models.ForeignKey(Message, null=True, blank=True, on_delete=models.CASCADE)


