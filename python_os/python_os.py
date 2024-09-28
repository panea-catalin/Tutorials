import os

print(os.name)

print(os.environ["SHELL"])
print(os.getenv("SHELL"))

#diff between the two is that if yhe key does not exist
#environ will print an error while getenv will print None
# print(os.getenv("SHELL2"))
# print(os.environ["SHELL2"])

#print current working dir
print(os.getcwd())
#change current working dir
os.chdir(r"../")
#print the new working dir
print(os.getcwd())

#create dir
# os.mkdir("test")
#or you can set a path and pass it to mkdir()
# path = "../"
# os.mkdir(path)

#create the dir structure(create directories that don't exist along the way)
# path = r'C:Users\user\pytest\dir1\dir2
# os.makedirs(path)

#remove files and directories
# os.remove("test.txt")
# or.rmdir("pytest")

#rename a file or folder
# os.rename("test.txt", "new_test.txt")

#"start" or open files
# os.startfile(r'C:\Users\use\file.pdf)

#iterate or list files and directories
# path = r'/'
# for root, dirs, files in os.walk(path):
#     print(root)
#     for _dir in dirs:
#         print(_dir)
#     for _file in files:
#         print(_file)

#paths
print(os.path.basename(r'/home/vancleef'))
print(os.path.dirname(r'/home/vancleef'))
#os.path.exists(r'path')
print(os.path.exists(r'/home/vancleef'))
#os.path.isdir/isfile
print(os.path.isdir(r'/home/vancleef'))
print(os.path.isfile(r'/home/vancleef'))
#os.path.join(r'path','extra path')
print(os.path.join(r'/home','vancleef'))
#os.path.split(r'path')
print(os.path.split(r'/home/vancleef'))
#
dirname, fname = os.path.split(r'/home/vancleef')
print(dirname)
print(fname)