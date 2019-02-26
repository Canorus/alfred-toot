import sys
from plistlib import readPlist
import json

query = sys.argv[1]

#print(query)

info = readPlist('info.plist')
instance = info['variables']['instance']
key_code = info['variables']['key_code']
access_key = info['variables']['access_key']
instance_t = ''
key_t = ''
acc_t = ''


if instance == '':
	instance_t = "Please input your instance address"
else:
	instance_t = "Your instance address is " + str(instance)

if key_code == '':
	key_t = "Please input your key code from instance credential page"
else:
	key_t = "Your key code is "+str(key_code)

if access_key == '':
	acc_t = "Please re run workflow to retrieve access code from instance"
else:
	acc_t = "Your access key is saved to workflow variables"

if access_key == '':
	res = {"items": [
			{
				"title":"Instance address",
				"subtitle":instance_t,
				"arg":query,
				"variables":{"type":"instance"}
			},
			{
				"title":"Key code",
				"subtitle":key_t,
				"arg":query,
				"variables":{"type":"code"}
			},
			{
				"title":"Access key",
				"subtitle":acc_t,
				"arg":query,
				"variables":{"type":"access"}
			}
		]}
else:
	res = {'items':[
		{
			'title':'compose new toot',
			'subtitle':'send new toot',
			'arg':query,
			'variables':{'type':'toot'}
		}
	]}

res_f = json.dumps(res)
print(res_f)