from django.test import TestCase
from .models import *

# Create your tests here.

class LocationTestClass(TestCase):

  def setUp(self):
    self.new_location = Location(name = 'Nairobi')

  def tearDown(self):
    Location.objects.all().delete()
    

  def test_instance(self):
    self.new_location.save_location()
    self.assertTrue(isinstance(self.new_location, Location))
  
  
  def test_save_location(self):
    self.new_location.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)>0)

  def test_delete_location(self):
    self.new_location.delete_location(1)
    locations = Location.objects.all()
    self.assertTrue(len(locations)==0)

  # def test_update_location(self):
  #   self.new_location.save_location()
  #   Location.update_location(1,'Mombasa')
  #   updated_location = Location.objects.get(id=1)
  #   self.assertEqual(updated_location, 'Mombasa')
    


