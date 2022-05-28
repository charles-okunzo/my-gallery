from django.test import TestCase
from .models import *

# Create your tests here.

class LocationTestClass(TestCase):

  def setUp(self):
    self.new_location = Location(name = 'Nairobi')

  def test_save_location(self):
    self.new_location.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)>0)


