import os

totalsize = 0

for filename in os.listdir('F:\python_programs\list-dictionary-string') :
    if not os.path.isfile(os.path.join('F:\python_programs\list-dictionary-string', filename)) :
        continue
        
    totalsize += os.path.getsize(os.path.join('F:\python_programs\list-dictionary-string', filename))
    # print(totalsize)    

print('final %s' % (totalsize)) # culminative size of files in the directory

# print(os.chdir('../list-dictionary-string'))
# print(os.getcwd())