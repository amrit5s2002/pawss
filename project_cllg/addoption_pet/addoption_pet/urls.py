from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from Pet.views import PetCreateView,PetDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pet.urls')),
    path('',include('User.urls')),
    path('',include('root.urls')),
    path('blog/',include('blog.urls')),
    path('pet_create/new/', PetCreateView.as_view(), name='pet_create'),
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet_profile'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
