# from bs4 import BeautifulSoup as BS
import requests
import json

URL = "http://newsline.kg/getNews.php?limit=30&last_dt=2022-07-04%2007:57:33.933739"



def get_data(url):
    response = requests.get(url)
    html = response.text
    news = json.loads(html)
    if news['data']:
        with open('news.json', 'w') as f:
            data = []
            for n in news['data']:
                record = {
                    'id': n['id'], 'id_site': n.get('id_site'),
                    'title': n.get('title'),
                    'category': n.get('category'),
                    'category_id': n.get('category_id'),
                    'desc': n.get('desc'),
                    'dt': n.get('dt'),
                    'img': n.get('img'),
                    'link': n.get('link'),
                    'date': n.get('date'),
                    'site_name': n.get('site_name')
                }
                data.append(record)
            json.dump(data, f, indent=4, ensure_ascii=False)

get_data(url=URL)


# print(get_response(url=URL))