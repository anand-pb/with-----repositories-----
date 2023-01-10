import re

# example 1
# bat_regex = re.compile(r'bat(wo)?man')

# mo = bat_regex.search('batwoman got an apprenticeship in the wayne enterprises, which is run by batman')

# print(mo.group())

# example 2
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

# mo = phone_regex.search('call me at 415-555-1234 tomorrow')
mo = phone_regex.search('call me at 555-1234 tomorrow')

print(mo.group())
