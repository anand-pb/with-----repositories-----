import re

# example '^'
# beginswith_regex = re.compile(r'^hello')

# mo = beginswith_regex.search('hello buddies over there!')

# print(mo.group())

# example '$'
# beginswith_regex = re.compile(r'there!$')

# mo = beginswith_regex.search('hello buddies over there!')

# print(mo.group())

# example
# alldigits_regex = re.compile(r'^\d+$')

# mo = alldigits_regex.search('9821347650')

# print(mo)

# example '.'
# endswith_regex = re.compile(r'.at')
# endswith_regex = re.compile(r'.{1,2}at')

# mo = endswith_regex.findall('the cat in a hat, sat on the flat mat')

# print(mo)

# example '.*' greedy matching
# name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')

# mo = name_regex.findall('First Name: anand Last Name: pb')

# print(mo)

# example '.*' non-greedy matching
# name_regex = re.compile(r'<(.*?)>')
# name_regex = re.compile(r'(.*)')

# mo = name_regex.findall('<to serve shawarma> for dinner')

# print(mo)

# example re.DOTALL
# msg = 'iron man suggests shawarma\ncap suggest brooklyn\nnat suggests budapest'
# print(msg)

# dotstar_regex = re.compile(r'.*')
# dotstar_regex = re.compile(r'.*', re.DOTALL)

# mo = dotstar_regex.search(msg)

# print(mo)

# example re.IGNORECASE
msg = 'Iron man suggests shawarma, cAp suggest brooklyn, nat suggests budapest'
# print(msg)

# dotstar_regex = re.compile(r'[aeiou]')
dotstar_regex = re.compile(r'[aeiou]', re.IGNORECASE)

mo = dotstar_regex.findall(msg)

print(mo)