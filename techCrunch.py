#! python3
#techCrunch.py- Scrapes Timestamp, News Title, Image Source URL, Author from 'The Latest' news articles on the homepage of TechCrunch.com


import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from dateutil import parser

#dictionary to store the final get_data
scraped_dict={}

def get_data():
    res = requests.get("https://www.techcrunch.com")
    try:
        soup=BeautifulSoup(res.content, "html.parser")

        #latest section data
        latest=soup.find(class_='river--homepage')

        #number of articles
        no_of_articles=0
        articles=latest.find_all('div',class_='post-block')
        for article in articles:
            no_of_articles+=1


        #article timestamp
        article_time_stamp=latest.find_all('time', class_="river-byline__time")

        #article title
        article_title=latest.find_all('h2', class_='post-block__title')

        #article image url
        article_image_url=latest.find_all('footer',class_="post-block__footer")

        #article authors
        article_authors=latest.find_all('span', class_="river-byline__authors")


        for article in range(no_of_articles):
            #list of content for each article
            each_article=[]

            #inserting article title
            each_article.append(article_title[article].find('a').get_text().strip())
            scraped_dict[article]=each_article

            #inserting article timestamp
            raw_datetime=article_time_stamp[article]['datetime']
            raw_datetime=parser.parse(raw_datetime).replace(tzinfo=timezone.utc).astimezone(tz=None)
            final_datetime=raw_datetime.strftime('%H:%M %p %Z %B %d, %Y')
            scraped_dict[article].append(final_datetime)


            #inserting article image url
            scraped_dict[article].append(article_image_url[article].findChildren('img')[0]['src'])

            #inserting article authors
            authors_list=[]
            for author in article_authors[article].find_all('a'):
                authors_list.append(author.get_text().strip())
            scraped_dict[article].append(", ".join(authors_list))

        return scraped_dict


    except Exception as exc:
        print("There was a problem: %s" %(exc))


if __name__=='__main__':
    get_data()



