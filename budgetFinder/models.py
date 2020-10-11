from django.db import models

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
