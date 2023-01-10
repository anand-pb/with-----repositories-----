import re

# example 1
# lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

# xmas_regex = re.compile(r'\d+\s\w+')

# mo = xmas_regex.findall(lyrics)

# print(mo)

# example 2
# vowel_regex = re.compile(r'[aeiouAEIOU]')

# mo = vowel_regex.findall('robocop eats baby food')

# print(mo)

# example 3
# vowel_regex = re.compile(r'[aeiouAEIOU]{2}')

# mo = vowel_regex.findall('robocop eats baby food')

# print(mo)

# example 4
vowel_regex = re.compile(r'[^aeiouAEIOU]')

mo = vowel_regex.findall('robocop eats baby food')

print(mo)