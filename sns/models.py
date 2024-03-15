from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Messageクラス
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,     \
                              related_name='message_owner')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    share_id = models.IntegerField(default=-1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_share(self):
        return Message.objects.get(id=self.share_id)

    class Meta:
        ordering = ('-pub_date',)


# Groupクラス
class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
                              related_name='group_owner')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# riendクラス

class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
                             related_name='friend_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' (group:"' + str(self.group) + '")'

# JoinFriendクラス
class Joinfriend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, \
                              related_name='friend_user')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    hope_date = models.DateTimeField(auto_now_add=True)
    join_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return str(self.user) + ' (group:"' + str(self.group) + '")'


# Goodクラス
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
                              related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for "' + str(self.message) + '" (by ' + \
               str(self.owner) + ')'


class Comment(models.Model):
    text = models.TextField("本文", blank=False)
    commented_at = models.DateTimeField("投稿日", auto_now_add=True)
    commented_to = models.ForeignKey(Message, verbose_name ='message',on_delete=models.CASCADE)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",
                                     on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.text
