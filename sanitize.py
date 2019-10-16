import re
import random

# a = 0
curSMS = None
data = []
with open('mysmsdata.txt','rb') as f:
  msg = ""
  for ln in f:
    # a += 1
    # if a is 50:
    #   break
    decoded=False
    line=''
    for cp in ('cp1252', 'cp850','utf-8','utf8'):
      try:
        line = ln.decode(cp)
        decoded=True
        break
      except UnicodeDecodeError:
        pass
    if decoded:
      matches = re.match('On :(\w\w\w-\d\d-\d\d\d\d)  At: (\d\d:\d\d) From :([\w\s]+):[\s]+', line)
      if matches:
        if curSMS:
          msg = msg.replace('\n',' ')
          msg = msg.replace('\r',' ')
          curSMS['msg'] = msg
          data.append(curSMS)
        msg = ""
        curSMS = {'on': matches.group(1), 'at': matches.group(2), 'from': matches.group(3)}
      else:
        msg += line

dataString = []
for datum in data:
  lineStr = "\t".join(datum.values())
  dataString.append(bytes(lineStr, 'utf-8'))

random.shuffle(dataString)
with open('sanitizedata.txt','wb') as f:
  for lineString in dataString:
    f.write(lineString)
    f.write(bytes('\n', 'utf-8'))
