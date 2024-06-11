from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from .utils import get_random_code
# Create your models here.

User=get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=250, default='O\'zinggiz haqida ...')
    avatar = models.ImageField(default='avatars/avatar.png',upload_to="profile/%Y/%m/%d")
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.username)
    
    def save(self, *args, **kwargs):
        ex=False
        if self.last_name and self.first_name:
            now_slug = slugify(str(self.last_name)+ " " +str(self.first_name))
            ex=Profile.objects.filter(slog=now_slug).exists()
            while ex:
                now_slug = slugify(str(self.last_name)+ " " +str(self.first_name)+ " " + str(get_random_code))
                ex=Profile.objects.filter(slog=now_slug).exists()
        else:
            now_slug=slugify(self.user)
        self.slug=now_slug
        return super(Profile, self).save(*args, **kwargs)


STATUS_CHOICES=(
    ('sender', 'sender'),
    ('accepted', 'accepted'),
)
class RelationShip(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.status)
    
    
    