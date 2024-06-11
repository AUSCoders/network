# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile, RelationShip

# @receiver(post_save, sender=User)
# def post_save_cerate_profile(sender, instance, created, **kwargs):
#     print("sender",sender)
#     print("instance",instance)
#     print("created",created)
#     if created:
#         Profile.objects.create(user=instance)
        
        
# @receiver(post_save, sender=RelationShip)
# def post_save_add_to_freands(sender, instance, created, **kwargs):
#     sender_=instance.sender
#     receiver_=instance.receiver
#     if instance.status=="accepted":
#         sender_.frinds.add(receiver_.user)
#         receiver_.frinds.add(sender_.user)
#         sender_.save()
#         receiver_.save()
        
        