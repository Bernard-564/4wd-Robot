import json
from urllib.request import urlopen
 
with urlopen("https://gbfs.citibikenyc.com/gbfs/en/station_information.json") as response: 
    source = response.read()
    
    print(source)