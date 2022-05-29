from django import views
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.home, name= 'home'),
  path('/search', views.search_by_category, name = 'search_results')
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

