from django.db import models

class Tags(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.code

class Status(models.Model):
    status = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.status

class Snippet(models.Model):
    tag = models.ManyToManyField(Tags, related_name='snippet')
    time_stamp = models.DateTimeField()
    topic = models.CharField(max_length=30)
    details = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {} : {}".format(self.topic, self.status, self.tag)