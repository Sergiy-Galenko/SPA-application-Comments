from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    homepage = models.URLField(blank=True, null=True)
    captcha = models.CharField(max_length=6)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.username}'

    @property
    def is_reply(self):
        return self.parent is not None
