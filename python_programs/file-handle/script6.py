import shelve

shelfFile = shelve.open('temp_data')

shelfFile['colors'] = ['orange', 'purple', 'gold', 'violet', 'gray']

shelfFile.close()