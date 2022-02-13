from email import header
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

url="https://www.billboard.com/charts/hot-100/"

date=input("what year you would like to travel to in YYY-MM-DD")
#**********************************************Code Dealing with Getting authenticated with Spotify API*************************************
CLIENT_ID="29b4aa34873d43e7a5fb0133a098c832"
CLIENT_SECRET="63c8b9a9dbe747f8814d4143b83c56be"

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri="http://example.com",scope=scope))

USER_ID=sp.current_user()['display_name']

#********************************************Code Dealing with Getting Billiboard Data In desirable form************************************
response=requests.get(url=url+date)
webpage=response.text

soup=BeautifulSoup(webpage,"html.parser")
raw_songs=soup.find_all(name="h3",id="title-of-a-story",class_="c-title")

songs=[song.getText() for song in raw_songs]
del songs[0:6]
start=1
end=start+3
while (end<len(songs)):
    del songs[start:end]
    start=start+1
    end=start+3

del songs[len(songs)-4:len(songs)]

final_songs=[song.split("\n")[1] for song in songs]

#*****************************************Code Dealing with Getting url of every Song from Spotify API************************************
songs_uri=[]
for song in final_songs:
    string_to_search="track:"+song+" year:"+date[0:4]
    result = sp.search(q=string_to_search, type="track")
    
    try:
        uri=result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify")

#creating playlist
PLAYLIST_ID=sp.user_playlist_create(user=USER_ID,name=f"{date} Billiboard 100", public=False,collaborative=False, description='Top 100 songs')["id"]

#adding tracks to the playlist
sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=songs_uri, position=None)





    