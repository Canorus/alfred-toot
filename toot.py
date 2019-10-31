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
# trim every 500 char, returns list
def trim(t):
    t_ = t.split(' ')
    a = list()
    s = ''
    n = 0
    for i in t_:
        if n + 1 + len(i) > 500:
            a.append(s.strip())
            s = i
            n = len(i)
        else:
            s += ' ' + i
            n += len(i) + 1
    a.append(s.strip())
    return a

if 'web' in keys:
    u = get_url()
    p['web'] = u
if 'prev' in keys:
    p['prev']=True
if 'cb' in keys:
    p['cb'] = True

def sendtoot(status, cw=None, visib='unlisted', web=None, cb=None, prev=None, to=None, *args):
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
    r = requests.post(instance + '/api/v1/statuses', headers=status_h, data=da)
    print(r.json()['id'])

if len(p['status']) < 500:
    sendtoot(**p)
else:
    t = p['status']
    sl = trim(t)
    for s in range(len(sl)):
        p1 = p
        if s == 0:
            p1['status'] = sl[s]
            sendtoot(**p1)
        else:
            p1['status'] = sl[s]
            p1['prev'] = True
            sendtoot(**p1)
