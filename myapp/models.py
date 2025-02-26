from django.db import models

# Create your models here.



class project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class testimonial(models.Model):
    name = models.CharField(max_length=100)
    feedback_text = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name