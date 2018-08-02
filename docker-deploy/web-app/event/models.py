from django.db import models
from django.contrib.auth.models import Permission, User

class Event(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,related_name = "user")
    event_name = models.CharField(max_length=250, null = True) #text
    event_time = models.DateField(null = True)
    event_invitation = models.ManyToManyField(User, related_name = "invitation")
    event_owner = models.ManyToManyField(User, related_name = "owner")
    event_vendor = models.ManyToManyField(User, related_name = "vendor")
    event_guest = models.ManyToManyField(User, related_name = "guest")
    location = models.CharField(max_length=10000, null = True)
    is_passed = models.BooleanField(default=False)
    support_plus_one = models.BooleanField(default=False)
    permit_plus_number = models.IntegerField(default=1)

    def __str__(self): #when call Eventname.objects.all(), it will print the event name
        return str(self.event_name) + '-' + str(self.event_time) + '-' + str(self.event_owner)

class TextQuestion(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    question = models.TextField(max_length=200)
    permit_vendor = models.ManyToManyField(User, related_name="permit_vendor")
    vendor_cansee = models.BooleanField(default=False)
    guest_canmodify = models.BooleanField(default=True)
    multi_choice = models.BooleanField(default=False)
    has_submitted = models.BooleanField(default=False)
    is_text = models.BooleanField(default=True)
    permit_choice_number = models.IntegerField(default = 1)

class TextAnswer(models.Model):
    answeruser = models.ForeignKey(User, default=1, on_delete=models.CASCADE,related_name = "answeruser")
    question = models.ForeignKey(TextQuestion, on_delete=models.CASCADE)
    answer = models.TextField(max_length=1000)

class Choice(models.Model):
    question = models.ForeignKey(TextQuestion, on_delete=models.CASCADE)
    choice_description = models.CharField(max_length=200)
    userchoose = models.ManyToManyField(User, related_name = "userchoose")

    def __str__(self): #when call Eventname.objects.all(), it will print the event name
        return str(self.choice_description)

class MultiAnswer(models.Model):
     answer_muti_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE,related_name = "answer_muti_user")
     question = models.ForeignKey(TextQuestion, on_delete=models.CASCADE)
     selected_choice = models.ManyToManyField(Choice, related_name = "selected_choice")

class PlusOne(models.Model):
    userchooseplusone = models.ForeignKey(User, default=1, on_delete=models.CASCADE,related_name = "userchooseplusone")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    you_want_plus = models.IntegerField(default = 0)

