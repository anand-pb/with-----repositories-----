myCat = {
    'size' : 'fat',
    'color' : 'orange',
    'sound' : 'loud'
}

print(myCat['color'])

print(myCat.keys())
print(myCat.values())
print(myCat.items())

blnv = 'size' in myCat.keys()

print(blnv)

blnv = 'weight' not in myCat.keys()

print(blnv)