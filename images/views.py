from django.shortcuts import render

from images.models import Image

# Create your views here.


def home(request):

  all_images = Image.objects.order_by('-created_at')
  all_categories = Image.objects.order_by('-category')
  all_locations = Image.objects.order_by('location')



  return render(request, 'index.html', {'all_images':all_images, 'all_categories':all_categories, 'all_locations': all_locations})