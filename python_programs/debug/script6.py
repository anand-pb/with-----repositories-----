import logging

logging.basicConfig(filename='program-logs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

logging.debug('start of program')

def factorial(n) :
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1) :
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('return value is %s' % (total))
    return total

print('enter a number')
num = input()
print(factorial(int(num)))

logging.debug('end of program')
