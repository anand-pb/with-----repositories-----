import re

bat_regex = re.compile(r'bat(man|mobile|copter|place)')

mo = bat_regex.search('batcopter repaired its turbine')
print(mo.group())