from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('CSE', 'Computer Science'), 
        ('EEE', 'Electrical and Electronics'), 
        ('ECE', 'Electronics and Communication'),
        ('MECH', 'Mechanical'),
        ('CIVIL', 'Civil')
    )

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='images/',  blank=True, null=True)
    video= models.FileField(upload_to='videos/', null=True, verbose_name="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name + ": " + str(self.profile_image)