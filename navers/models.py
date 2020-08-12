from django.db import models

# Create your models here.
JOB_ROLE_CHOICES = [
    (1,'Desenvolvedor'),
    (2,'Engenheiro de software'),
    (3,'DBA'),
    (4,'Gerente de projetos'),
    (5,'DevOps'),

]
class Naver(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nome')
    birthdate = models.DateField('Data de nascimento')
    admission_date = models.DateField('Data de admissão')
    job_role = models.IntegerField(choices=JOB_ROLE_CHOICES,default=1,verbose_name='Cargo')
    user = models.ForeignKey('users.User',related_name='navers',on_delete=models.PROTECT)
