from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length =30,null=True)
    company = models.CharField(max_length =30,null=True)
    email = models.EmailField()
    APPLICANT_CHOICES=(
        ('EMPLOYER','employer'),
        ('EMPLOYEE','employee'),
    )
    applicants=models.CharField(
        max_length=20,
        choices=APPLICANT_CHOICES,
    )
    job=models.CharField(max_length=50,null=True)
    descriptions=models.TextField(max_length=200,null=True)
    pay=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    picture = models.ImageField(upload_to='avatar/', default='default.jpg')
    post = HTMLField(null=True)
    contact=models.PositiveIntegerField(null=True)


    @classmethod
    def search_by_job(cls,search_term):
        applicants = cls.objects.filter(job__icontains=search_term)
        return applicants

class User(models.Model):
    name=models.CharField(max_length=50,null=True)
    user_email=models.EmailField(max_length=50,null=True)
class Profile(models.Model):
    name = models.CharField(max_length=70,null=True)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='profile')
    profile_pic = models.ImageField(upload_to='image/', default='default.png')
    bio=models.TextField(max_length=500,null=True )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.name


    @classmethod
    def all_profiles(cls):
        profiles = cls.objects.all()
        return profiles
