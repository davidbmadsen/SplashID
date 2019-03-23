from bs4 import BeautifulSoup as bs
import requests


def get_search(qstring, results):

    base = "https://www.youtube.com/results?search_query="
    r = requests.get(base + qstring)

    page = r.text
    soup = bs(page, 'html.parser')

    vids = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})

    videolist = []
    for v in vids:
        tmp = 'https://www.youtube.com/watch?v=' + v['href']
        videolist.append(tmp)
    return videolist[0:results]

print(get_search('yee',3))

