import os
import shutil

for directoryname, subdirectory, filename in os.walk('F:\\python_programs\\file-handle') :
    print('the directory is ' + directoryname)
    print('the sub-directories in ' + directoryname + ' are ' + str(subdirectory))
    print('the filenames in ' + directoryname + ' are ' + str(filename))
    print('\n')

    # for subdir in subdirectories :
    #     os.unlink(subdir)

    for file in filename :
        if file.endswith('.py') :
            shutil.copy(os.path.join(directoryname, file), os.path.join('F:\\python_programs\\file-handle\\backup_example', file + '.backup')) 