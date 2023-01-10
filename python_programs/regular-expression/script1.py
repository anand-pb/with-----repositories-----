import re

phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phonenumregex.search('call me at 415-555-1011 tomorrow')
print(mo.group())

# print(phonenumregex.findall('call me at 415-555-1011 tomorrow'))