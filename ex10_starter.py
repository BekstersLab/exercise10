# import built in modules for file operations - system, global, operating system
import glob
import sys
import os

# EXERCISE 1a: Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# sys.platform determines OS on which Python interpreter is running and returns string representing the name eg.
# Windows: 'win32'
# Linux: 'linux' or 'linux2
# MacOS: 'darwin'
# Unix: FreeBSD - 'freebsd', Solaris - 'sunos5' etc
# hdir - variable holds path to home directory of user
# use if/else conditional statements to determine the users directory
# if - Windows first as uses a particular path separator
# else - all other systems as there are numerous that use the same path separator that is different to Windows

# Construct a portable wildcard pattern
# wild card is a symbol that can be used in place of or in addition to one or more characters

pattern = os.path.join(hdir, '*')
# SO... above code joins home directory path with wildcard character '*' to create a pattern that matches ...
# all files and directories inside the home directory
# os.path.join() function - concatenates paths for os running python (Windows or Linux)
# uses correct path separator for os eg '/' on Unix/Linux/macOS and '\' on Windows
# '*' - wildcard character - matches any sequence of characters in a filename. * means ALL


# os.path.join() function - concatenates paths for os running python (Windows or Linux)
# uses correct path separator for os eg '/' on Unix/Linux/macOS and '\' on Windows
# '*' - wildcard character - matches any sequence of characters in a filename. * means ALL
# SO... above code joins home directory path with wildcard character '*' to create a pattern that matches ...
# all files and directories inside the home directory
# Output of code:
# \C:\Users\username\* - windows
# /home/username/* - unix/linux/macOS


# TODO: Use the glob.glob() function to obtain the list of filenames

filenames = glob.glob(pattern)
# glob.glob returns a list of files that matches the path specified in the function argument
# relative path to search all text files
# uses wildcard character * to match all filepath to the current file


# Output of code:
# \C:\Users\username\* - windows
# /home/username/* - unix/linux/macOS

print('Inside current directory')
for item in glob.glob("*"):
    print(item)

# print function used to display string object in the console.
print('Inside current directory')
# for loops iterate through a sequence of each file found in the specified glob.glob module and function
for files in glob.glob("*"):
    # prints each filename in the exercise10 file
    print(files)


# TODO: use os.path.getsize to find each file's size
#  os.path.getsize(filepath) is used to get the size of the file

# Created a list called file paths to define the files which want to use the os modul function
file_paths = ['ex10_starter.py', '.gitignore', 'README.md']

# for loop used through iterable object (like list, tuple, set etc.) in file_paths
# list specified as file_path as necessary to have in
for file_path in file_paths:
    # we use the os.path.getsize method to find the size of the file
    size = os.path.getsize(file_path)
    # print('Size of files:', file_path, size)
    # print with f string the size of the file on the console
    print(f"Size of '{file_path}':", size)

# TODO: Add a test to only display files that are not zero length
# file_paths = ['ex10_starter.py', '.gitignore', 'README.md']

# for loop to iterate a list because if not, it only counts
for file_path in file_paths:
    # write the function of this module != not equal to zero
    if os.path.getsize(file_path) != 0:
        # write about print function with f-string
        print(f'{file_path} is not equal to zero')
        # issue - there is no end to indented line

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

# added file path with directory name
filepath = "C:/code/python_homework/exercise10/ex10_starter.py"
basename = os.path.basename(filepath)
print(basename)


# # ////// Bek's Updated Code in full //////
#
# # code below is fixed and now shows any files with content directly in the home directory
# # think it should be in current directory?
#
# # check for OS using if/else statement
# # 'HOME' and 'HOMEPATH' are environment variables - path points to users home directory
# if sys.platform == 'win32':
#     hdir = os.environ['HOMEPATH']
# else:
#     hdir = os.environ['HOME']
#
# # create search pattern to find files. '*' wildcard means "anything" to match any file/directory in user home directory
# pattern = os.path.join(hdir,'*')
#
# # find files and directories that match pattern. Returns list of paths
# filenames = glob.glob(pattern)
#
# # use for loop to iterate over each file/directory found by glob.glob()
# for filename in filenames:
#     # added code below to check if path is a file rather than a directory
#     if os.path.isfile(filename):
#         # if it is a file get the size
#         size = os.path.getsize(filename)
#         # if size greater than 0 bytes print name of file
#         if size > 0:
#             # print just the file name not the full path
#             print(os.path.basename(filename))
