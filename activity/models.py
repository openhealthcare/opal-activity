"""
Models for activity
"""
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.timesince import timesince as timesince
from django.db import models


class Activity(models.Model):
    actor = models.ForeignKey(User)
    verb  = models.CharField(max_length=200)
    
    action_content_type = models.ForeignKey(ContentType, related_name='action_contenttype')
    action_object_id = models.PositiveIntegerField()
    action_object = generic.GenericForeignKey('action_content_type', 'action_object_id')    
    
    target_content_type = models.ForeignKey(ContentType, related_name='target_contenttype')
    target_object_id = models.PositiveIntegerField()
    target_object = generic.GenericForeignKey('target_content_type', 'target_object_id')

    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def timesince(self):
        return timesince(
            self.timestamp, None).encode('utf8').replace(b'\xc2\xa0', b' ').decode('utf8')
