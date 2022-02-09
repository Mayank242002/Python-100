from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
all_articles=soup.find_all(name="a",class_="titlelink")
all_articles_upvote=soup.find_all(name="span",class_="score")
articles_texts=[]
articles_links=[]
for article in all_articles:
    article_text=article.getText()
    articles_texts.append(article_text)
    article_link=article.get('href')
    articles_links.append(article_link)

all_upvotes=[]
for upvote in all_articles_upvote:
    all_upvotes.append(upvote.getText())


required_all_upvotes=[]
for upvote in all_upvotes:
    required_all_upvotes.append(int(upvote.split(" points")[0]))

greatest_vote=max(required_all_upvotes)
index=required_all_upvotes.index(greatest_vote)
print(greatest_vote)
print(len(all_articles_upvote))
print(len(articles_texts))
print(required_all_upvotes)
print(articles_texts[index],articles_links[index])




'''Note:as one articles does not have any upvote , results might be diffrent'''


















'''file=open("Day-45 Web-Scraping using Beautifull soap/index.html","r")
content=file.read()

soup=BeautifulSoup(content,'html.parser')
 
for link  in soup.find_all(name='a'):
    print(link.getText())


image=soup.find(name="img",class_="bottom-cloud")
print(image.get("class"))'''