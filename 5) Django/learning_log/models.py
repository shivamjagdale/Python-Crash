from django.db import models

# Create your models here.

# Topic 

class Topic(models.Model):

    # text 
    text = models.CharField(max_length=100)

    # date_added
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

# Entry 
class Entry(models.Model):

    # Foreign Key
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # text 
    text = models.TextField()

    # date_added
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.text[:50]}.........."