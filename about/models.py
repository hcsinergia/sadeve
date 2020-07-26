from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model

from apps.socio.models import Socio

User = get_user_model()

class BoardMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    chair = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email #+' ' + self.user.last_name
		#return self.user.username


class About(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    init_year = models.CharField(max_length=10, blank=True, null=True)
    end_year = models.CharField(max_length=10, blank=True, null=True)
    about_description = HTMLField()
    president = models.OneToOneField(BoardMember, related_name="c_member_president", on_delete=models.CASCADE, blank=True, null=True)
    vicepresident = models.OneToOneField(BoardMember, related_name="c_member_videpresident", on_delete=models.CASCADE, blank=True, null=True)
    secretary = models.OneToOneField(BoardMember, related_name="c_member_secretary", on_delete=models.CASCADE, blank=True, null=True)
    treasurer = models.OneToOneField(BoardMember, related_name="c_member_treasurer", on_delete=models.CASCADE, blank=True, null=True)
    vocal_sr = models.OneToOneField(BoardMember, related_name="c_member_vocal_sr", on_delete=models.CASCADE, blank=True, null=True)
    vocal_jr = models.OneToOneField(BoardMember, related_name="c_member_jr", on_delete=models.CASCADE, blank=True, null=True)
    accounter_sr_1 = models.OneToOneField(BoardMember, related_name="c_member_acc_sr_1", on_delete=models.CASCADE, blank=True, null=True)
    accounter_sr_2 = models.OneToOneField(BoardMember, related_name="c_member_acc_sr_2", on_delete=models.CASCADE, blank=True, null=True)
    accounter_jr = models.OneToOneField(BoardMember, related_name="c_member_acc_jr", on_delete=models.CASCADE, blank=True, null=True)
    about_honor_associates = models.CharField(max_length=500)
    about_life_associates = models.CharField(max_length=500)
    about_active_associates = models.CharField(max_length=500)
    about_protector_associates = models.CharField(max_length=500)
    about_follower_associates = models.CharField(max_length=500)


    def __str__(self):
        return self.title
