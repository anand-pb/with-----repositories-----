print('how many cats do you have ?')
numCats = input()

try :
    if int(numCats) >= 4 :
        print('thats a lot of cats')

    else :
        print('that is not that many cats')        

except ValueError :
    print('you did not enter a number')    