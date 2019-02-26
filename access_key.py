import os
from plistlib import readPlist, writePlist
import requests
import json

code = os.getenv('key_code')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
instance = os.getenv('instance')
auth_data = {'client_id':client_id,'client_secret':client_secret,'code':code,'grant_type':'authorization_code','redirect_uri':'urn:ietf:wg:oauth:2.0:oob'}
rauth = requests.post(instance+'/oauth/token',data=auth_data)
access = rauth.json()['access_token']
info = readPlist('info.plist')
info['variables']['access_key'] = access
writePlist(info, 'info.plist')