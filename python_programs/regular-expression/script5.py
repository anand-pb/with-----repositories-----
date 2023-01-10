import re

# example 1 (zero or more no. of repetition)
# bat_regex = re.compile(r'bat(m)*man')

# mo = bat_regex.search('lets not call him batmmmmman, not even batmman, but batman')

# print(mo.group())

# example 2 (one or more no. of repetition)
# bat_regex = re.compile(r'bat(m)+man')

# mo = bat_regex.search('lets not call him batmmmmman, not even batmman, but batman')

# print(mo.group())

# example 3 (exactly 'x' no. of repetition)
# phone_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){1,3}')

# mo = phone_regex.search('call me at 415-555-1234 tomorrow, or at 344-4567-3210 today, or at 987-5555 anytime')

# print(mo.group())

# example 4 greedy match
# digit_regex = re.compile(r'(\d){3,5}')

# mo = digit_regex.search('3458765')

# print(mo.group())

# example 5 non-greedy match
digit_regex = re.compile(r'(\d){3,5}?')

mo = digit_regex.search('3458765')

print(mo.group())