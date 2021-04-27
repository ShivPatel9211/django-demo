from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    Fullname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True,blank= True)

class Blog_post(models.Model):
    sno=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = HTMLField() 
    image = models.ImageField(upload_to="static")
    slug = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.slug} {self.author}"
 
class Comment(models.Model):
    sno=models.AutoField(primary_key=True)
    post = models.ForeignKey(Blog_post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    parent=models.ForeignKey('self',on_delete=models.CASCADE ,null=True , related_name='+')
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment,self.user)
