from django.db import models

# Create your models here.

class message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    messageText = models.CharField(max_length=2000)

    def __str__(self):
        return self.id, self.name
