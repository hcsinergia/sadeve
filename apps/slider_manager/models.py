from django.db import models

class slider(models.Model):
    img1 = models.ImageField(blank=True, null=True)
    img2 = models.ImageField(blank=True, null=True)
    img3 = models.ImageField(blank=True, null=True)
    img4 = models.ImageField(blank=True, null=True)
 
    # def __str__(self):
    #     return self.user.email #+' ' + self.user.last_name
	# 	#return self.user.username

class banner_socios_protectores(models.Model):
    img1 = models.ImageField(blank=True, null=True)
    img2 = models.ImageField(blank=True, null=True)
    img3 = models.ImageField(blank=True, null=True)
    img4 = models.ImageField(blank=True, null=True)