def boxPrint (symbol, width, height) :
    if len(symbol) != 1 :
        raise Exception('"symbol" needs to be string of length 1')
    
    if (width < 2) or (height < 2) :
        raise Exception('"width" and "height" must be greater than or equal to 2')
    print(symbol * width)

    for i in range(height -2) :
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


print('enter symbol')
s = input()

print('enter width')
w = input()

print('enter height')
h = input()

boxPrint(str(s), int(w), int(h))        
