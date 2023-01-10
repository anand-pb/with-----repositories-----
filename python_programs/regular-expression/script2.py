# groups in regex

import re

phonenumregex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

mo = phonenumregex.search('call me at 415-555-1011 tomorrow')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))