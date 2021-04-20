"""audioServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from audioFiles import views
from audioFiles import api_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    
    #path('audioFiles/<str:audioFileTypes>/<int:id>', views.audio_details, name = 'song_details'),
    path('audioFiles/song/<int:id>', views.song_details, name = 'song_details'),
    path('audioFiles/audiobook/<int:id>', views.audiobook_details, name = 'audiobook_details'),
    path('audioFiles/podcast/<int:id>', views.podcast_details, name = 'podcast_details'),
    
    # path('audioFiles/api', api_view.audioList.as_view()),
    # path('audioFiles/api/new/song', api_view.audioCreate.as_view()),
    #path('audioFiles/api/song/<int:id>', api_view.songRetrieveUpdateDestroy.as_view()),
    path('audioFiles/api/create/<str:audioFileType>', api_view.audioCreate, name = 'audioCreate'),
    path('audioFiles/api/view/<str:audioFileType>', api_view.audioAll, name = 'audioAll'),
    path('audioFiles/api/view/<str:audioFileType>/<int:id>', api_view.audioDetails, name = 'audioDetails'),
    path('audioFiles/api/update/<str:audioFileType>/<int:id>', api_view.audioUpdate, name = 'audioUpdate'),
    path('audioFiles/api/delete/<str:audioFileType>/<int:id>', api_view.audioDelete, name = 'audioDelete'),
    
]
