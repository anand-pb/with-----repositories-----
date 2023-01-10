txtfile = open('F:\\python_programs\\file-handle\\textfile_w.txt', 'w') 
# 'w' - write mode, 'a' - append mode

txtfile.write('written in write mode A\n')
txtfile.write('written in write mode B')

txtfile.close()