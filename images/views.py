from django.shortcuts import render

from images.models import Image

# Create your views here.


def home(request):

  all_images = Image.objects.order_by('-created_at')
  all_categories = Image.objects.order_by('category')



  return render(request, 'index.html', {'all_images':all_images, 'all_category':all_categories})