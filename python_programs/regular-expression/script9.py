import re

# names_regex = re.compile(r'Agent \w+')

# mo = names_regex.findall('Agent Alice gave the secret documents to Agent Bob')
# print(mo)

# mo = names_regex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob')
# print(mo)

# example
names_regex = re.compile(r'Agent (\w)\w*')

mo = names_regex.findall('Agent Alice gave the secret documents to Agent Bob')
# print(mo)

mo = names_regex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob')
print(mo)