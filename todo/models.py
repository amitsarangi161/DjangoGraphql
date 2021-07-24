from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=1, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}---- {self.name}"
