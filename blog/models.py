from django.utils import timezone
from django.conf import settings
from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    # Publish Action Method
    def publish(self):
        self.published_at = timezone.now()
        self.save()

    # String Format
    def __str__(self):
        return self.title