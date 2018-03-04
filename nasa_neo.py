#!/bin/python3
#geektechstuff
#NASA NEO
#Big thanks to NASA API (https://api.nasa.gov/api.html), get your API key from this site.

import json, urllib.request

#variables
api='DEMO_KEY'
start_date=""
end_date=""
result=""
potentially_hazardous=""

#message to welcome the user
print('Hi and welcome to GeekTechStuff\'s NASA Near Earth Object (NEO) Python program')
print('This programme uses NASA\'s open API system')
print('')

#asks the users for dates, these must be in yyyy-mm-dd format
start_date=input('Please enter an eight digit date in yyyy-mm-dd format for the start date:')
end_date=input('Please enter an eight digit date in yyyy-mm-dd format for the end date:')

#opens JSON file containing NEO data
url='https://api.nasa.gov/neo/rest/v1/feed?start_date='+start_date+'&end_date='+end_date+'&api_key='+api
response=urllib.request.urlopen(url)
result=json.loads(response.read())
print('Loading data from',url)
print('')

#uses the json loaded from get_json
print('There were',result['element_count'],'NEO\'s between',start_date,'and',end_date)

