import os
import sys

__all__ = ['-p', '-mds', '-i', '-o']

__help__ = """first argument is file name
-p         provides a path but is not necessary if this is not provided it will deafult to current path 
-i         will ignore warning such as file overwrite warnings etc 
-mds       will create a new directory containg the file you must provide 
-p         with the path when using mds
-o         will automatically open the file after creation this will open in preffered editor for each file type(may give error warning ignore)
?/-help    shows this help message

Examples:
Example 1: "touch filename.type"         this will create a filename in the current working directory
Example 2: "touch filename.type -i"      this will create a filename in the current working directory and "-i" will ignore warnings such as file already exists
Example 3: "touch filename.type -p       path\path\example" -p will change the current directory to the provided path instead of the current directory
Example 4: "touch filename.type -p       test\meme -mds" "-mds"this will create the directories and place file inside it
Example 5: "touch filename.type -o" "-o" will open the file after creation"""


__example__ ="""Example 1: "touch filename.type"         this will create a filename in the current working directory
Example 2: "touch filename.type -i"      this will create a filename in the current working directory and "-i" will ignore warnings such as file already exists
Example 3: "touch filename.type -p       path\path\example" -p will change the current directory to the provided path instead of the current directory
Example 4: "touch filename.type -p       test\meme -mds" "-mds"this will create the directories and place file inside it
Example 5: "touch filename.type -o" "-o" will open the file after creation"""


path = os.getcwd() 

args = sys.argv

args.pop(0)
if '-help' in args or '?' in args:
    print(__help__)
    sys.exit()
mds = False


if '-mds' in args:
    mds = True
    if not '-p' in args:
        print('You must provide a path using -p when using -mds type -help or ? for help')
        sys.exit()
warn = True
if '-i' in args:
    warn = False
open_ = False
if '-o' in args:
    open_ = True
try:
    name = args[0]
except:
    print('Error file name should be the first argument type -help or ? for help')
    sys.exit()

for i in args:
    if i not in __all__:
        if not i[0] == '-':
            continue
        print('Invalid argument ' + str(i) + ' type -help or ? for help')
        sys.exit()
if '-p' in args:
    try:
        path = args[args.index('-p') + 1]
        if not os.path.exists(path):
            if mds:
                """ new_dir = remvfile(path) """
                os.makedirs(path)
            else:
                print('Non existant path')
                sys.exit()
    except:
        print('please provide path after -p')
comp = path + '\\' + name
if os.path.exists(comp):
    if warn:
        # print('y')
        while True:
            q = input(f'file {comp} already exists in {path} would you like to overwrite it? y/n add -i to ignore warnings:').lower()

            if q == 'y':
                break
            elif q == 'n':
                sys.exit()
with open(comp, 'w') as file:
    file.write('')
if open_:
    os.startfile(comp)

