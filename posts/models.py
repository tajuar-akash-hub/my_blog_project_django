from django.db import models
from catagories.models import Catagory
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    catagory = models.ManyToManyField(Catagory)
    # this means, one catagory can have multiple post also,
    # multiple post can have one catagory
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # on_delete=models.CASCADE for : if user delete his/her account,all post will be deleted

    def __str__(self) -> str:
        return f'{self.title}'







