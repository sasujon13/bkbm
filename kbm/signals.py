from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Dept, Gallary

@receiver(post_save, sender=Dept)
def ensure_all_depts_have_gallary(sender, instance, **kwargs):
    # Go through all Depts and create Gallary if missing
    for dept in Dept.objects.all():
        Gallary.objects.get_or_create(Dept=dept)
