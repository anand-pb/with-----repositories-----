import re, pyperclip

# regex for phone numbers
phone_regex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
(\s|-)                  # first separator
\d\d\d                  # first 3 digits
-                       # separator
\d\d\d\d                # last 4 digits
(((ext(\.)?\s)|x)       # extension word-part (optional)
(\d{2,5}))?             # extension number-part (optional)
)
''', re.VERBOSE)

# regex for email
email_regex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# get the text on the clipboard
text = pyperclip.paste()

# extract phone number and email from the text on clipboard
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)
# print(extracted_email)

allphonenumber = []
for phonenumber in extracted_phone :
    allphonenumber.append(phonenumber[0])

# print(allphonenumber)

# copy to clipboard
results = '\n'.join(allphonenumber) + '\n'.join(extracted_email)
pyperclip.copy(results)
# print(results)    
