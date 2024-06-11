from django.db import models
# from users.models import Profile
from posts.models import Post
# Create your models here.



class Comment(models.Model):
    # user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    body=models.TextField(max_length=500)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.pk)