#!/usr/bin/python
import urllib3
import datetime
import xmltodict
url = 'http://www.yr.no/sted/Tsjekkia/Annet/Litultovice/varsel_time_for_time.xml'

def homepage():

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    #data = BeautifulSoup(response)
    data = xmltodict.parse(response.data)
    return data['weatherdata']['forecast']['tabular']['time']


if __name__ == '__main__':
    data= homepage()
    for radek in data:
        #print radek['temperature']['@value']
        d = datetime.datetime.strptime(radek['@from'], '%Y-%m-%dT%H:%M:%S')
        print str(d) + ' ' + radek['temperature']['@value']