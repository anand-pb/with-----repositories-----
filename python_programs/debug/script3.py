import traceback

try :
    raise Exception('this is the error message')

except :
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('the traceback info was written error_log.txt')        