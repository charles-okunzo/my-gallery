from django.shortcuts import render

from images.models import Image

# Create your views here.


def home(request):

  all_images = Image.objects.order_by('-created_at')
  all_categories = Image.objects.order_by('-category')
  all_locations = Image.objects.order_by('location')



  return render(request, 'index.html', {'all_images':all_images, 'all_categories':all_categories, 'all_locations': all_locations})


def search_by_category(request):
  if 'image_by_cat' in request.GET and request.GET['image_by_cat']:
    search_phrase = request.GET.get('image_by_cat')
    searched_images = Image.search_image(search_phrase)
    message = f'{search_phrase}'

  else:
    message = 'You haven\'t searches for any images' 

  return render(request, 'search_category.html', {'searched_images': searched_images, 'message': message})