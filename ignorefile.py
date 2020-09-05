import os
from os import listdir
from os.path import isfile, join

#Globally ignored files
globalignore = ['bin', 'lib', 'lib64', 'include', '__pycache__']
#Files which are specifically allowed by a specific ignorefile
specificallow = {'.gitignore': ['.git']}

path = str(input('Enter path for script: '))
if os.path.exists(path):
    #Ignorefiles to create with script
    ignorefilelist = []
    while True:
        filename = str(input('Enter filenames (e.g. .dockerignore, .gitignore) one at a time, or enter "D" for done: '))
        if filename in ['d', 'D']:
            break
        else:
            ignorefilelist.append(filename)
    
    ignorefiles = {}
    for f in ignorefilelist:
        ignorefiles[f] = open(path + '/' + f, "w")
    
    folderlist = []
    filelist = []

    for i in specificallow:
        globalignore += specificallow[i]

    for f in listdir(path):
        written = []
        if f in globalignore or f in list(ignorefiles.keys()):
            for i in ignorefiles: 
                if f != i and (i not in specificallow or (i in specificallow and f not in specificallow[i])):
                    ignorefiles[i].write(f + '\n')
                    written.append(i)
            print(f + ' added to ' + ', '.join(written))
        else:
            if isfile(join(path, f)):
                filelist.append(f)
            else:
                folderlist.append(f)

    for f in folderlist + filelist:
        written = []
        while True:
            userchoice = str(input('Should ' + f + ' be added to ' + ', '.join(list(ignorefiles.keys())) + '? (Yes/No/Modify): ')).lower()
            if userchoice in ['y', 'yes']:
                for i in ignorefiles:
                    ignorefiles[i].write(f + '\n')
                    written.append(i)
                break
            elif userchoice in ['n', 'no']:
                break
            elif userchoice in ['m', 'modify']:
                for i in ignorefiles:
                    while True:
                        userchoice = str(input('Should ' + f + ' be added to ' + i + '? (Yes/No): ')).lower()
                        if userchoice in ['y', 'yes']:
                            ignorefiles[i].write(f + '\n')
                            written.append(i)
                            break
                        elif userchoice in ['n', 'no']:
                            break
                        else:
                            print("Sorry, I didn't understand that")
                            continue
                break
            else:
                print("Sorry, I didn't understand that")
                continue

        if len(written) != 0:
            print(f + ' added to ' + ', '.join(written))

    for i in ignorefiles:
        ignorefiles[i].close()
    print('Done!')
else:
    print('Path does not exist!')