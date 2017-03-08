from django.db import models

# Create your models here.
class Commentary(models.Model):
    class Meta:
        db_table = 'guestbook_commentary'

    name = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.name + " : " + self.text

    def __unicode__(self):
        return self.name + " : " + self.text