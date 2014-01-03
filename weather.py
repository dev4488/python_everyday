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
	result = json.loads(r.tedatat)
	if result['cod']=='404':
		print 'Error:city not found,please check name of city',sys.edatait()
	else:
		return result


if __name__ == '__main__':
	if len(sys.argv)<2 or len(sys.argv)>2 :
		print  'Error --format: ''./mausam.py city_name '
	else:
		data = Weather(sys.argv[1])
		#prints various data fields
		print 'Weather |',data['name'],data['sys']['country'],'at',
		print (datetime.datetime.fromtimestamp(int(data['dt'])).strftime('%H:%M:%S %m-%d-%Y '))
		print '   ''temp:',data['main']['temp']
		print '   ''humidity:',data['main']['humidity']
		weather = data['weather']
		print '  ',[i for i in weather[0].values()][3]
		print '   ''wind speed:',data['wind']['speed']
	
