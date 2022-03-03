#author: LM (AMDG) 2/8/22

open_file = open('alma_mater.txt', 'r')
while True:
    line = open_file.readline()
    if len(line) == 0:
        break
    for value in line:
        print('\n')
        
        print('\n')

        print(line, end='')