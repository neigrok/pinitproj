from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    class Meta:
        db_table = 'note1'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_url = models.CharField(max_length=60)
    note_title = models.CharField(max_length=100)
    note_text = models.CharField(max_length=600)
    note_tags = models.CharField(max_length=150)
    note_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note_title

    def __unicode__(self):
        return self.note_title


class NoteShare(models.Model):
    class Meta:
        db_table = 'noteshareobj'
    sharing_userid = models.CharField(max_length=20)
    shorten_url = models.CharField(max_length=8)

    def __str__(self):
        return 'from' + self.sharing_userid

    def __unicode__(self):
        return 'from' + self.sharing_userid