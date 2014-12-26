from django.db import models
import datetime

class Fact(models.Model):
    text = models.TextField(
        max_length=316,
        help_text="maximum 316 characters long"
        )
    timestamp = models.DateTimeField(default=datetime.datetime.now())


    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ["-timestamp"]