from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile, RelationShip

User=get_user_model()

@receiver(post_save, sender=User)
def post_save_cerate_profile(sender, instance, created, **kwargs):
    print("sender",sender)
    print("instance",instance)
    print("created",created)
    user=instance
    if created:
        Profile.objects.create(user=instance,username=user.username,email=user.email,first_name= user.first_name,last_name = user.last_name).save()
        
        
@receiver(post_save, sender=RelationShip)
def post_save_add_to_freands(sender, instance, created, **kwargs):
    sender_=instance.sender
    receiver_=instance.receiver
    if instance.status=="accepted":
        sender_.frinds.add(receiver_.user)
        receiver_.frinds.add(sender_.user)
        sender_.save()
        receiver_.save()
        
        