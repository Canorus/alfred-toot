import sys
from plistlib import readPlist
import requests
import unicodedata
import re

toot = sys.argv[1]
info = readPlist('info.plist')
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
    print(toot_sp)
    toot_split = re.findall('!.*?:',toot)
    for i in range(len(toot_split)):
        toot_split[i] = toot_split[i][1:-1]
    print(toot_split)
    toot_split.insert(0,'status')
except:
    hd['status']=toot
    split = 0

try:
    toot_split[toot_split.index('cw')] = 'spoiler_text'
except:
    pass

try:
    toot_split[toot_split.index('visib')] = 'visibility'
except:
    pass

if split:
    for i in range(len(toot_sp)):
        hd[toot_split[i]] = unicodedata.normalize('NFC',toot_sp[i])

if 'clipboard' in toot_split or 'cb' in toot_split:
    media_id = ''
    print('clipboard attachment detected')
    clipboard_image()
    print('media_id outside function is '+media_id)
    try:
        del hd['clipboard']
    except:
        del hd['cb']
    hd['media_ids[]']=media_id

st = requests.post(instance+'/api/v1/statuses',data=hd,headers=status_h)
print(st.json())
