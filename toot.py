import sys
import re
import json
import requests
import unicodedata
from plistlib import load

i = sys.argv[1]

info = load(open('info.plist','rb'))
instance = info['variables']['instance']
access = info['variables']['access_key']
status_h = {'Authorization':'Bearer '+access}

visib = info['variables']['visibility']

keys = re.findall(" !.*?:",i)
if len(keys):
    values = re.compile(" !.*?:.*?").split(i)
    for j in range(len(keys)):
        keys[j] = keys[j][2:-1]
    keys.insert(0,'status')
    p = dict()
    for key in range(len(keys)):
        p[keys[key]] = unicodedata.normalize('NFC',values[key].strip())
else:
    p = {'status':unicodedata.normalize('NFC',i)}

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
    r = requests.post(instance+'/api/v1/media',headers=status_h, files=files)
    print(r.status_code)
    media_id = r.json()['id']
    return media_id

def get_prev():
    account_id = requests.get(instance+'/api/v1/accounts/verify_credentials',headers=status_h).json()['id']
    prev_status = requests.get(instance+'/api/v1/accounts/'+account_id+'/statuses',headers=status_h).json()[0]
    return prev_status

def get_url():
    try:
        import subprocess
        currentTabUrl = str(subprocess.check_output(['osascript','browser.scpt']))[2:-3]
        url = currentTabUrl
        if currentTabUrl == 'browser not in front':
            raise
        return url # might need encoding. later
    except:
        pass

if 'web' in keys:
    u = get_url()
    p['web'] = u
if 'prev' in keys:
    p['prev']=True
if 'cb' in keys:
    p['cb'] = True
if 'base' in keys:
    p['base'] = True

def sendtoot(status, cw=None, visib=visib, web=None, cb=None, prev=None, to=None, base=None, *args):
    da = dict()
    da['status'] = status
    if cw:
        da['spoiler_text'] = cw
    da['visibility'] = visib
    if web: # input is url
        da['status'] += '\n\n' + str(web)
    if to:
        da['in_reply_to_id'] = to
    if prev:
        prev_stat = get_prev()
        da['in_reply_to_id'] = prev_stat['id']
        if not cw:
            da['spoiler_text'] = prev_stat['spoiler_text']
        if not visib:
            da['visibility'] = prev_stat['visibility']
    if cb:
        media_id = clipboard_image()
        da['media_ids[]'] = media_id
    if base:
        import base64
        da['status'] = base64.encodestring(da['status'].encode('utf-8')).decode('utf-8')
    r = requests.post(instance + '/api/v1/statuses', headers=status_h, data=da)
    print(r.json()['id'])

sendtoot(**p)
