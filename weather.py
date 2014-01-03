#!/usr/bin/env python
import requests
import json
import sys
import datetime

#TODO: make GUI 

def Weather(city_name):
	query = 'http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric' % city_name
	r = requests.get(query)
	result = json.loads(r.text)
	if result['cod']=='404':
		print 'Error:city not found,please check name of city',sys.exit()
	else:
		return result


if __name__ == '__main__':
	if len(sys.argv)<2 or len(sys.argv)>2 :
		print  'Error --format: ''./mausam.py city_name '
	else:
		x = Weather(sys.argv[1])
		print 'Weather |',x['name'],x['sys']['country'],'at',
		print (datetime.datetime.fromtimestamp(int(x['dt'])).strftime('%H:%M:%S %m-%d-%Y '))
		print '   ''temp:',x['main']['temp']
		print '   ''humidity:',x['main']['humidity']
		weather = x['weather']
		print '  ',[i for i in weather[0].values()][3]
		print '   ''wind speed:',x['wind']['speed']
	
