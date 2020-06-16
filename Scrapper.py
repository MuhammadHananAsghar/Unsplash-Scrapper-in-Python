'''CREATED BY MUHAMMAD HANAN ASGHAR
DATA SCIENTIST
PYTHONIST
'''
import requests
from bs4 import BeautifulSoup as Soup
import json
#import scrapy
def unSplash(a):
    newval = ""
    if " " in a:
        list_search = [i for i in a]
        for i in range(len(list_search)):
            if " " == list_search[i]:
                list_search[i] = "+"
        newval = "".join(list_search)
    else:
        newval = a
    print(newval)
    html_data = requests.get(f"https://unsplash.com/napi/search/photos?query={newval}&xp=&per_page=20&page=1")
    html = html_data.content
    jsons = json.loads(html)
    total_pages = jsons['total_pages']
    if total_pages > 50:
        pages = 10
    else:
        pages = total_pages
    print(pages)
    images = []
    for i in range(pages):
        html = requests.get(f"https://unsplash.com/napi/search/photos?query={newval}&xp=&per_page=20&page={i+1}")
        data = json.loads(html.content)
        values = []
        for i in range(len(jsons['results'])):
            value = jsons['results'][i]
            values.append(value)
        for i in range(len(values)):
            value = values[i]['urls']['full']
            images.append(value)
    return images
wall = unSplash("sunny")
