# -*- coding: utf-8 -*-
import sys
from plistlib import load
import requests
import unicodedata
import re
import json

try:
    reply = sys.argv[1]
except:
    reply = ""
info = load(open('info.plist', 'rb'))
access = info['variables']['access_key']
instance = info['variables']['instance']
head = {'Authorization': 'Bearer '+access}

notis = json.loads(requests.get(
    instance+'/api/v1/notifications', headers=head).content.decode('utf-8'))

def strip(t):
    t = re.sub('</p><p>', '\n', t)
    t = re.sub('(<.?p>|<.?a.*?>|<.?span.*?>)', '', t)
    t = re.sub('&lt;', '<', t)
    t = re.sub('&gt;', '>', t)
    t = re.sub('&apos;', '\'', t)
    t = re.sub('&quot;', '\'', t)
    t = re.sub('<br.*?\/?>', '\n', t)
    return t

items = list()
for noti in notis:
    if noti["type"] == 'mention':
        item = dict()
        item["title"] = strip(noti['status']['content'])
        item["subtitle"] = "from: "+str(noti['account']['acct'])
        if noti['status']['mentions']:
            mention = ['@'+i['acct'] for i in noti['status']['mentions']]
            mention.append('@'+str(noti['account']['acct']))
        else:
            mention = []
        item["arg"] = '{"status":"'+str(reply)+'","in_reply_to_id":"'+str(noti['status']['id'])+'","acct":"'+' '.join(mention)+'"}'  # list 어떻게 넘겨야 되지
        items.append(item)
results = {"items": items}
print(json.dumps(results))