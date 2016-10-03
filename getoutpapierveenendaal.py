

from bs4 import BeautifulSoup
import urllib.request
r = urllib.request.urlopen('http://www.afvalscheiden-bestapart.nl/papier').read()

soup = BeautifulSoup(r)

for element in soup.findAll('table')[0].findAll('tr'):
   location = str(element.findAll("td")[0].findAll(text=True)[0]) 
   print(location,end=' ') 
   location = str(element.findAll("td")[1].findAll(text=True)[0]) 
   print(location,end='') 
   print('",\n"',end='')


print("\n\nEnd of list!!!\n\n")
for element in soup.findAll('table')[0].findAll('tr'):
   location = str(element.findAll("td")[1].findAll(text=True)[0]) 
   print(location,end='') 
   print('",\n"',end='')




print("\n\nEnd of list!!!\n\n")

from geopy.geocoders import Nominatim
geolocator = Nominatim()
for element in soup.findAll('table')[0].findAll('tr'):
   desc = str(element.findAll("td")[0].findAll(text=True)[0]) 
   desc+=" "+  str(element.findAll("td")[1].findAll(text=True)[0]) 
   location = str(element.findAll("td")[1].findAll(text=True)[0]) 
   location = geolocator.geocode(location + " veenendaal")
   if location != None:
     print("{lat:"+str(location.latitude)+",lng:"+str(location.longitude)+",desc:'"+ desc+"'},")

