import requests
import json

WIKI = "https://en.wikipedia.org/w/api.php"

def make_query(category):
	
	payload = {
	'action' : 'query', 
	'list' : 'categorymembers', 
 	'cmtitle' : category,
 	'format': 'json',
 	'cmlimit':500
 	}

	return payload

def make_search_list(category):
	res = requests.get(WIKI, params = make_query(category))
	out_list = []
	for entry in res.json()['query']['categorymembers']:
		out_list.append(entry['title'])

	return out_list


village_list = make_search_list("Category:Villages_in_England_by_county")
hamlet_list = make_search_list("Category:Hamlets_in_England_by_county")

uk_places_list = village_list + hamlet_list

###goes through the county list to find villages
for places in uk_places_list:
	print("searching", places)
	place_request = requests.get(WIKI, params = make_query(places))
	
	places_list = place_request.json()['query']['categorymembers']

	for place in places_list:
		print('\t',place['title'])		
		with open('uk_village_names.txt','a') as village_file:
			village_file.write(place['title'] +'\n')

print(len(places_list))