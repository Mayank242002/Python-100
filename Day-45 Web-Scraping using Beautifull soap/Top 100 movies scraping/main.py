from urllib import response
import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.timeout.com/film/best-movies-of-all-time")
webpage=response.text


soup=BeautifulSoup(webpage,"html.parser")
Movies=soup.find_all(name="h3",class_="_h3_cuogz_1")
Movies_name=[movie.getText() for movie in Movies]

file=open("Day-45 Web-Scraping using Beautifull soap/Top 100 movies scraping/movies.txt","w")
for movie in Movies_name:
    file.write(movie+"\n")

file.close()