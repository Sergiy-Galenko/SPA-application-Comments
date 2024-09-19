from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    homepage = models.URLField(blank=True, null=True)
    captcha = models.CharField(max_length=6)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.username}'
