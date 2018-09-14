import requests
import sys
from plistlib import readPlist, writePlist
import webbrowser

address = sys.argv[1]
if address[0:8] != 'https://':
    address = 'https://'+address

#put instance address to environmental variables
info = readPlist('info.plist')
info['variables']['instance'] = address
writePlist(info, 'info.plist')

client_name = 'Alfred'
data = {'client_name':client_name,'redirect_uris':'urn:ietf:wg:oauth:2.0:oob','scopes':'write'}
r = requests.post(address+'/api/v1/apps',data=data)

if r.status_code != 200:
    print('error')
else:
    rdata = r.json()
    client_id = rdata['client_id']
    client_secret = rdata['client_secret']
    # saving credentials to environmental variables
    info['variables']['client_id'] = client_id
    info['variables']['client_secret'] = client_secret
    writePlist(info, 'info.plist')
    #open authentication page
    webbrowser.open(address+'/oauth/authorize?client_id='+client_id+'&redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=code&scope=write')