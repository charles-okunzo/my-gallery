from django.db import models
# from cloudinary.models import CloudinaryField
# Create your models here.

class Location(models.Model):
  name = models.CharField(max_length=30)


  def __str__(self) -> str:
    return f'{self.name}'


  def save_location(self):
    self.save()


  def delete_location(self, location_id):
    Location.objects.filter(id= location_id).delete()
  
  @classmethod
  def update_location(cls, location_id, updated_name):
    cls.objects.filter(id=location_id).update(name = updated_name)


class Category(models.Model):
  name = models.CharField(max_length=30)

  def save_category(self):
    self.save()

  def delete_category(self, category_id):
    Category.objects.filter(id= category_id).delete()

  @classmethod
  def update_category(cls, category_id, updated_name):
    cls.objects.filter(id=category_id).update(name = updated_name)


  def __str__(self) -> str:
    return f'{self.name}'


class Image(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
  category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
  created_at = models.DateTimeField(auto_now_add=True)
  image_path = models.ImageField(upload_to='photos', null=True)


  def save_image(self):
    self.save()

  def delete_image(self, image_id):
    Image.objects.filter(id= image_id).delete()

  @classmethod
  def update_image(cls, image_id, updated_name):
    cls.objects.filter(id=image_id).update(name = updated_name)


  def __str__(self) -> str:
    return f'{self.name}'