import sys
from plistlib import load
import requests
import json
import unicodedata

data = json.loads(sys.argv[1])
info = load(open('info.plist','rb'))
access = info['variables']['access_key']
instance = info['variables']['instance']
head = {'Authorization':'Bearer '+access}
data['status'] = str(data['acct'])+' '+unicodedata.normalize('NFC',data['status'])
t = requests.post(instance+'/api/v1/statuses',data=data,headers=head)
