from django.db.models.signals import post_save

from users.models import Profile, User


def save_profile_user(sender, **kwargs):
    print(kwargs)
    if kwargs['created']:
        profile_user = Profile.objects.create(user=kwargs['instance'])
        print(profile_user)
        profile_user.save()


post_save.connect(save_profile_user, sender=User)
