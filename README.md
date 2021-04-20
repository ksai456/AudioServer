# audioServer
This is my first Python-Django project

This is a Django Web API that simulates the behavior of an audio file server while using a SQL database(sqlite used).

Tools Needed :

python
pip install django
pip install djangorestframework


Usage :

Download git audioServer repository  to local directory 

1.go to audioServer Folder
2.To run run django server run the command
  - python manage.py runserver
  
Go to web browser
Urls:
http://localhost:port/ - Home page --> Displays all songs, audiobooks, podcasts in HTML template format
    
http://localhost:port/audioFiles/song/id  -> id=1, 2, 3 to display specified song in HTML template format
http://localhost:port/audioFiles/audiobook/id  -> id=1, 2, 3 to display specified audiobook in HTML template format
http://localhost:port/audioFiles/podast/id  -> id=1, 2, 3 to display specified song in HTML template format
    
http://localhost:port/audioFiles/api/create/<str:audioFileType>  --> audioFileType can be any one of {song, audiobook, podcast}
This is create api url for adding song/audiobook/podcast
song json format to supply to add in DB

{
    "audiofiletype": "[]",
    "name_of_the_song": "[]",
    "duration_in_number_of_seconds": [],
    "uploaded_time": "[]"
}

audiobook json format:
{
    "audiofiletype": "Audiobook",
    "title": "[]",
    "author": "[]",
    "narrator": "[]",
    "duration_in_number_of_seconds": [],
    "uploaded_time": "[]"
}

podcast format:

{
    "audiofiletype": "Podcast",
    "duration_in_number_of_seconds": 90000,
    "uploaded_time": "[]",
    "name_of_the_podcast": "[]",
    "host": "[]",
    "participants": "[]"
}

Eg for creating a song :
http://127.0.0.1:8000/audioFiles/api/create/song

{
    "audiofiletype": "Song",
    "name_of_the_song": "Song name",
    "duration_in_number_of_seconds": 360,
    "uploaded_time": "2021-04-20T12:27:06Z"
}

http://localhost:port/audioFiles/api/view/<str:audioFileType> --> audioFileType can be any one of {song, audiobook, podcast}
This api let's you view all songs/audiobook/podcast stored in DB.
Eg: http://127.0.0.1:8000/audioFiles/api/view/song --> This api will let you view all songs in json format

http://localhost:port/audioFiles/api/view/<str:audioFileType>/<int:id> --> audioFileType can be any one of {song, audiobook, podcast} and id=1,2,3...
This api let you to view specific audiofile type of given id
Eg: http://127.0.0.1:8000/audioFiles/api/view/song/1  --> retrieve song details with id 1
{
    "audiofiletype": "Song",
    "id":1,
    "name_of_the_song": "Song name",
    "duration_in_number_of_seconds": 360,
    "uploaded_time": "2021-04-20T12:27:06Z"
}

http://localhost:port/audioFiles/api/update/<str:audioFileType>/<int:id> --> audioFileType can be any one of {song, audiobook, podcast} and id=1,2,3...
This api let you to update specific audiofile type of given id
Eg : http://127.0.0.1:8000/audioFiles/api/update/song/1
{
    "audiofiletype": "Song",
    "id":1,
    "name_of_the_song": "Song name- updated song name",
    "duration_in_number_of_seconds": 360,
    "uploaded_time": "2021-04-20T12:27:06Z"
}

http://localhost:port/audioFiles/api/delete/<str:audioFileType>/<int:id> --> audioFileType can be any one of {song, audiobook, podcast} and id=1,2,3...
This api let you to delete specific audiofile type of given id
Eg : http://127.0.0.1:8000/audioFiles/api/delete/song/1  --> this will delete the song with 1d = 1
