import json
import requests

url = ('https://newsapi.org/v2/top-headlines?'
	'country=in&'
	'q=covid&'
	'pageSize=5')

headers = {'X-Api-Key': '588992b6c6cc45bb9a133f7d7d009041'}
response = requests.get(url, headers=headers)

data = json.loads(response.content)

news_title_urls = {}
for i in range(len(data['articles'])):
	title = data['articles'][i]['title']
	title = title[:title.find("-")]
	news_title_urls[title] = data['articles'][i]['url']
