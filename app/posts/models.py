from django.db import models
# from users.models import Profile
from django.core.validators import FileExtensionValidator

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    image=models.ImageField(upload_to="post/",  validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
    # liked=models.ManyToManyField(Profile, blank=True, related_name="liked")
    # author=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    post_updated=models.DateTimeField(auto_now=True)
    post_created=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    # get liked cound num 
    # def get_liked(self):
        # return self.liked.all().count()
    # get commit all count number 
    def get_commit_number(self):
        return self.comment_set.all().count()
    
    class Meta:
        ordering=['post_updated', "post_created"]
        
        
    

LIKE_CHOICES=(
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)
class Like(models.Model):
    # user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user}--{self.post}-{self.value}"