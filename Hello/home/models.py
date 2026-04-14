from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    
    email = models.CharField(max_length=122)
    
    phone = models.CharField(max_length=12)
    
    desc = models.TextField()
    
    date = models.DateField()
    
    
    def __str__(self):
        return self.name
    
"""    
class Image(models.Model):
     image = models.ImageField(upload_to='images/', blank=True, null=True)
     image_url = models.URLField(blank=True, null=True)

def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url
        """