from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('姓名',max_length=30)
    age = models.IntegerField('年龄')
    email = models.EmailField('电子邮件')


    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题',max_length=100)
    author = models.ForeignKey('Person',verbose_name='作者',related_name='author_name',on_delete=models.PROTECT)  #一对多
    content = models.TextField('内容')
    score = models.IntegerField(verbose_name='分数')
    tags = models.ManyToManyField('Tag','标签名') #多对多

    publishTime = '123'

    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField('标签名',max_length=50)

    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.name