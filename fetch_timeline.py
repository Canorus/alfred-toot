import sys
from plistlib import load
import requests
import json
import re

# Authentication
info = load(open('info.plist','rb'))
access = info['variables']['access_key']
instance = info['variables']['instance']
head = {'Authorization':'Bearer '+access}

param = {'limit':50}

timelines = json.loads(requests.get(instance+'/api/v1/timelines/home',headers=head,params=param).content.decode('utf-8'))

def strip(t):
    t = re.sub('</p><p>','\n',t)
    t = re.sub('(<.?p>|<.?a.*?>|<.?span.*?>)','',t)
    t = re.sub('&lt;','<',t)
    t = re.sub('&gt;','>',t)
    t = re.sub('&apos;','\'',t)
    t = re.sub('&quot;','\'',t)
    t = re.sub('<br.*?\/?>','\n',t)
    return t

items = list()
for timeline in timelines:
    item = dict()
    item["title"] = strip(timeline['content'])
    item["subtitle"] = "from: "+str(timeline['account']['acct'])
    item["arg"] = timeline['id']
    items.append(item)
results = {"items":items}
print(json.dumps(results))
