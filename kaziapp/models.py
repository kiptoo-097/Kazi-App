from django.db import models

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
