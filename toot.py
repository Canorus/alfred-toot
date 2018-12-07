import sys
from plistlib import load
import requests
import unicodedata
import re

toot = sys.argv[1]
#info = readPlist('info.plist')
info = load(open('info.plist','rb'))
access = info['variables']['access_key']
instance = info['variables']['instance']
status_h = {'Authorization':'Bearer '+access}
hd = dict()

def clipboard_image():
    import io
    from PIL import ImageGrab
    buff = ImageGrab.grabclipboard()
    img = io.BytesIO()
    try:
        buff.save(img,format='PNG')
    except:
        print('Image is not in the most recent clipboard')
        return
    img = img.getvalue()
    files = {'file':img}
    r = requests.post(instance+'/api/v1/media',headers=status_h,files=files)
    print(r.status_code)
    global media_id
    media_id = r.json()['id']
    print('media_id in function is '+media_id)

split = 1

try:
    toot_sp = re.compile(" !.*?:.?").split(toot)
    toot_split = re.findall(' !.*?:',toot)
    for i in range(len(toot_split)):
        toot_split[i] = toot_split[i][2:-1]
    toot_split.insert(0,'status')
except:
    # if finding param breaks
    # just make status into hd dic
    # else it will be handled after converting params
    hd['status']=toot
    split = 0

# alternatives
try:
    toot_split[toot_split.index('cw')] = 'spoiler_text'
except:
    pass

try:
    toot_split[toot_split.index('visib')] = 'visibility'
except:
    pass

try:
    toot_split[toot_split.index('cb')] = 'clipboard'
except:
    pass

try:
    toot_split[toot_split.index('to')] = 'in_reply_to_id'
except:
    pass

# make params into hd dic

if split:
    for i in range(len(toot_sp)):
        hd[toot_split[i]] = unicodedata.normalize('NFC',toot_sp[i])

if 'prev' in toot_split:
    account_id = requests.get(instance+'/api/v1/accounts/verify_credentials',headers=status_h).json()['id']
    #print(requests.get(instance+'/api/v1/accounts/verify_credentials',headers=status_h).json())
    prev_status = requests.get(instance+'/api/v1/accounts/'+account_id+'/statuses',headers=status_h).json()[0]['id']
    hd['in_reply_to_id']=prev_status

if 'clipboard' in toot_split:
    media_id = ''
    clipboard_image()
    try:
        del hd['clipboard']
    except:
        del hd['cb']
    hd['media_ids[]']=media_id

if 'in_reply_to_id' in toot_split and 'silent' not in toot_split:
    import json
    who_reply_to = json.loads(requests.get(instance+'/api/v1/statuses/'+hd['in_reply_to_id']).content.decode('utf-8'))['account']['acct']
    hd['status'] += ' @'+who_reply_to

#print('hd is '+str(hd))
st = requests.post(instance+'/api/v1/statuses',data=hd,headers=status_h)
print(st.json())
