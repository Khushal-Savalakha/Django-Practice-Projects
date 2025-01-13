from django.db import models

# Create your models here.
class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set when a chat is created
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    username = models.CharField(max_length=255, default="null")  # New field for username

    def __str__(self):
        return f"{self.username}: {self.content} at {self.timestamp}"

class Group(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
