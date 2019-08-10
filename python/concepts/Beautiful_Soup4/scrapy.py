from bs4 import BeautifulSoup
import requests

# getting the source code of requested website.
# '.text' is added to get the source code in text format.
source = requests.get('http://coreyms.com').text

# Creating BS4 object by passing the source code and a parser.
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# Using inspect tool of browser to find the specific tag.
for article in soup.find_all('article'):
    # Picking required information using the parent tag i.e. article:
    # print(article.prettify())

    headline = article.header.h2.a.text
    print(headline)

    body = article.find('div', class_='entry-content').p.text
    print(body)

    try:
        # accessing 'src' attribute of 'iframe' tag as key of a dictionary.
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # getting the vid_id from the string.
        vid_id = vid_src.split('?')[0].split('/')[-1]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()
