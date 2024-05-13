# network


<details>

<summary>DB DIOGRAMMALAR</summary>

## Django boshlang'ich Tushncha va diogrammalar
![image](https://github.com/AUSCoders/network/assets/144318530/62e24f8b-91d1-4a33-aee5-5c847d825c55)


Profile models

```python
import string
import random
from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .utils import get_random_code
# Create your models here.


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Profile(models.Model):
    last_name=models.CharField(max_length=150, blank=True)
    first_name=models.CharField(max_length=150, blank=True)
    bio=models.TextField(max_length=600, default="O\'zinggiz haqida ma\'lomot....")
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    frinds=models.ManyToManyField(User, blank=True, related_name="frindes")
    email=models.EmailField(max_length=250, blank=True)
    avater=models.ImageField(default="avatar.png", upload_to="avatars/")
    country=models.CharField(max_length=120, default="Hi")
    slug=models.SlugField(blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.last_name}-{self.first_name}-{self.created}"
    def get_posts_number(self):
        return self.post_set.all().count()
    
    def get_authors_posts(self):
        return self.post_set.all()
    def get_likes_number(self):
        likes=self.like_set.all()
        total_like=0
        for item in likes:
            if item.value=="Like":
                total_like+=1
        return total_like
    def get_likes_recieved_number(self):
        post=self.post_set.all()
        total_like=0
        for item in post:
            total_like+=item.liked.all().count()
        return  total_like
                
    def save(self, *args, **kwargs) -> None:
        ew=None
        if self.first_name and self.first_name :
            to_slug=slugify(str(self.last_name).lower()+""+str(self.first_name)+""+str(get_random_code()))
            ew=Profile.objects.filter(slug=to_slug).exists()
            while ew:
                to_slug=slugify(str(rand_slug)+""+str(to_slug)+""+str(get_random_code()))
                ew=Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug=slugify(str(rand_slug)+""+str(get_random_code()))
        self.slug=to_slug
        return super().save(*args, **kwargs)


STATUS_CHOICES=(
    ("send", "send"),
    ("accepted", "accepted")
)
class RelationShip(models.Model):
    sender=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status=models.CharField(max_length=9, choices=STATUS_CHOICES)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.sender}-{self.receiver}-{self.status}"
    
    
    
    
   
```

</details>
