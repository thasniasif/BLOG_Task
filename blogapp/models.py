from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20,blank=True)
    date=models.DateTimeField()
    content=models.CharField(max_length=1000,blank=True)
    content_slice=models.CharField(max_length=500,blank=True)
    class Meta:
        db_table="blog_tb"
