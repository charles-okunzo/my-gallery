from django.db import models
# from cloudinary.models import CloudinaryField
# Create your models here.




class Image(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
  category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
  created_at = models.DateTimeField(auto_now_add=True)
  image_path = models.ImageField(upload_to='photos', null=True)