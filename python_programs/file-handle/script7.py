import shutil

# copy file from one directory to another directory
shutil.copy('F:\\python_programs\\file-handle\\folder1\\textfile1.txt', 'F:\\python_programs\\file-handle\\folder2')

# copy and rename
shutil.copy('F:\\python_programs\\file-handle\\folder1\\textfile2.txt', 'F:\\python_programs\\file-handle\\folder2\\textfile2-5.txt')

# copy directory from one directory to another directory
shutil.copytree('F:\\python_programs\\file-handle\\folder1', 'F:\\python_programs\\file-handle\\folder2\\folder2_backup')

# move file from one directory to another directory
shutil.move('F:\\python_programs\\file-handle\\folder1\\textfilex.txt', 'F:\\python_programs\\file-handle\\folder2')

# renaming a file
shutil.move('F:\\python_programs\\file-handle\\folder1\\textfilea.txt', 'F:\\python_programs\\file-handle\\folder1\\textfilea-b.txt')