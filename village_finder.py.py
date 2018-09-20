import requests
import json

WIKI = "https://en.wikipedia.org/w/api.php"

def make_query(category, cont_code):
	
	payload = {
	'action' : 'query', 
	'list' : 'categorymembers',
	'cmtitle' : category,
	'format': 'json',
	'cmlimit': 500,
	'cmcontinue': cont_code
	}
	return payload

def api_call(category, cont_code):	
	out_list = []
	res = requests.get(WIKI, params = make_query(category, cont_code))
	for entry in res.json()['query']['categorymembers']:
		out_list.append(entry['title'])

	try:
		cont_code = res.json()['continue']['cmcontinue']
	except:
		cont_code = None

	return out_list, cont_code

		
def wiki_search(category):
	category_list, cont_code = api_call(category, None)
	
	if cont_code != None:
		category_list += api_call(category, cont_code)[0]

	print('\tFound', len(category_list), 'places.')
	return category_list


places_list = wiki_search("Category:Villages_in_England_by_county")
places_list += wiki_search("Category:Hamlets_in_England_by_county")

###goes through the county list to find villages
village_list = []
for place in places_list:
	print("searching", place)
	village_list += wiki_search(place)
	
for counter, village in enumerate(village_list):
	village_name = village.split(',',1)[0].split('(',1)[0] #ugly-ass code turns  "Place, County" into "Place" or "Place (County)"" into "place"	 
	
	if counter % 100 == 0:
		print('Saving', counter , 'of', len(village_list))

	if 'Category:' not in village_name and 'List of' not in village_name: #removes further (/recursive) lists of lists.			
		with open('english_village_names.txt','a') as village_file:
			village_file.write(village_name +'\n')