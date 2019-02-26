import requests
import sys
from plistlib import load

toot = sys.argv[1] # toot id
info = load(open('info.plist','rb'))
instance = info['variables']['instance']
access = info['variables']['access_key']
status_h = {'Authorization':'Bearer '+access}

#print(access)

st = requests.post(instance+'/api/v1/statuses/'+toot+'/reblog',headers=status_h)
print(st.json())
