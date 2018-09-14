import sys
from plistlib import readPlist
import requests
import unicodedata
import re

# 'visibility': 'direct','private','unlisted','public' optional
# '!visibility: '
# will have to count calculation

toot = sys.argv[1]
info = readPlist('info.plist')
access = info['variables']['access_key']
instance = info['variables']['instance']

try:
    toot_sp = toot.split(' !cw: ')
    toot = toot_sp[0]
    cw_message = toot_sp[1]
except:
    cw_message = ''
status_h = {'Authorization':'Bearer '+access}
toot = unicodedata.normalize('NFC',toot)
status_cont = {'status':toot,'spoiler_text':cw_message}
st = requests.post(instance+'/api/v1/statuses',data=status_cont,headers=status_h)
