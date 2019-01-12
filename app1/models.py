from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()


    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.name+'    -    '+str(self.age)

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Person,on_delete=models.PROTECT)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.name