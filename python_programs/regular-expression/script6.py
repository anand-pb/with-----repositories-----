import re

# example findall() 
phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phone_regex.findall('call me at 415-555-1234 tomorrow, or at 344-456-3210 today, or at 555-987-5555 anytime')

print(mo)