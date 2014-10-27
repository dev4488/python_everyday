#!/usr/bin/env python
import requests
import json
import sys
import datetime

#TODO: make GUI 

def Weather(city_name):
	#openweathermap.com #API
	query = 'http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric' % city_name
	r = requests.get(query)
	#loads data from API in json format
	result = json.loads(r.text)
	if result['cod']=='404':
		print 'Error:city not found,please check name of city',sys.exit()
	else:
		return result


if __name__ == '__main__':
	if len(sys.argv)<2 or len(sys.argv)>2 :
		print  'Error --format: ''./weather.py city_name '
	else:
		data = Weather(sys.argv[1])
		#prints various data fields
		print 'Weather |',data['name'],data['sys']['country'],'at',
		print (datetime.datetime.fromtimestamp(int(data['dt'])).strftime('%H:%M:%S %m-%d-%Y '))
		print '\ttemp:',data['main']['temp']
		print '\thumidity:',data['main']['humidity']
		weather = data['weather']
		print '\t',[i for i in weather[0].values()][3]
		print '\twind speed:',data['wind']['speed']
	
