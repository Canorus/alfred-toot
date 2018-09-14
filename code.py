import sys
from plistlib import readPlist, writePlist

code = sys.argv[1]
info = readPlist('info.plist')
info['variables']['key_code'] = code
writePlist(info,'info.plist')