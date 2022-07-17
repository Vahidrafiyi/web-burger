
from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=120)
    alt = models.TextField(default='')
    image = models.ImageField(upload_to='store_image/sliders_image/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def save(self, *args, **kwargs):
        self.alt = self.title + ' متن تست '
        super().save(*args, **kwargs)  # Call the "real" save() method.



    def __str__(self):
        return self.title
