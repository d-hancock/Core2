from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from shop.models import Shop


#@receiver(post_save, sender=Profile)
#def create_shop(sender, instance, created, **kwargs):
  #  if created:
  #      Shop.objects.create(profile=instance)
