import requests
import json
from pprint import pprint
data= requests.get('https://api.mocki.io/v1/b043df5a')
data= json.loads(data.text)
pprint(data)
myList=[]
for n in range(len(data)):
 myList.append(data[n]['city'])
print(sorted(myList))