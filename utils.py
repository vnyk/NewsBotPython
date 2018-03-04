from wit import Wit 
from gnewsclient import gnewsclient

access_token = "SB3OXJRVDCTZDZO6JW3FQFCVBF2TLKVL"

client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	categories = {'newstype':None, 'location':None}
	entity=None
	value=None
	try:
		entity=list(resp['entities'])[0]
		value=resp['entities'][entity][0]['value']
		entities = list(resp['entities'])
		for entity in entities:
			categories[entity] = resp['entities'][entity][0]['value']
		
	except:
		pass

	return(entity,value,categories)


def get_news_elements(categories):
	news_client = gnewsclient()
	news_client.query = ''

	if categories['newstype'] != None:
		news_client.query += categories['newstype'] + ' '

	if categories['location'] != None:
		news_client.query += categories['location']

	news_items = news_client.get_news()

	elements = []

	for item in news_items:
		element = {
					'title': item['title'],
					'buttons': [{
								'type': 'web_url',
								'title': "Read more",
								'url': item['link']
					}],
					'image_url': item['img']		
		}
		elements.append(element)

	return elements