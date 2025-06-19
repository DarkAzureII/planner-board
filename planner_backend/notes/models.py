from django.db import models

class Note(models.Model):
    content = models.TextField()
    x = models.IntegerField(default=100)
    y = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Connection(models.Model):
    source = models.ForeignKey(Note, related_name='outgoing_connections', on_delete=models.CASCADE)
    target = models.ForeignKey(Note, related_name='incoming_connections', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)