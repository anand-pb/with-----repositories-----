import re

# explanation
    # (\d\d\d-) |   # area code (without parens, with dash)
    # (\(\d\d\d) )  # -or- area code with parens and no dash
    # \d\d\d        # first 3 digits
    # -             # second dash  
    # \d\d\d\d      # last 4 digits
    # \sx\d{2,4}    # extension, like x1234

phonenum_regex = re.compile(r'''
(\d\d\d-)|   # area code (without parens, with dash)
\((\d\d\d)\) # -or- area code with parens and no dash
\d\d\d       # first 3 digits
-            # second dash
(\d\d\d\d)     # last 4 digits
\sx\d{2,4}   # extension, like x1234
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)

mo = phonenum_regex.findall('call me at 415-555-1234 tomorrow, or at 344-456-3210 today, or at 555-987-5555 anytime')

print(mo)
