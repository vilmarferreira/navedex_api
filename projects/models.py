from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50,verbose_name='Nome')
    navers = models.ManyToManyField('navers.Naver', related_name='projects')
    user = models.ForeignKey('users.User',related_name='projects_list',on_delete=models.PROTECT)

    def as_json(self):
        return {
            "id":self.id,
            "name":self.name,
        }
