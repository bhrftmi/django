from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    is_enabled = models.BooleanField(default=False)
    publish_date = models.DateField(null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}- {}'.format(self.pk,self.title)


class comment(models.Model):
    post = models.ForeignKey(post , on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
