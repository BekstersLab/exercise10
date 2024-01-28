# Code below will list all non-empty files in the user's home directory, displaying their names without full path
# eg. Music, Pictures, Desktop, Libray, Public, Movies, Applications, Documents, Downloads

# import built in modules for file operations - system, global, operating system
import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# sys.platform determines the operating system on which Python interpreter is running and returns a string representing the name eg.
# Windows: 'win32'
# Linux: 'linux' or 'linux2
# MacOS: 'darwin'
# Unix: FreeBSD - 'freebsd', Solaris - 'sunos5' etc
# hdir - variable holds path to home directory of user
# use if/else statement to determine the users directory
# if - Windows first as uses a particular path separator
# else - all other systems as there are numerous that use the same path separator that is different to Windows

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
# os.path.join() function - concatenates paths for os running python (Windows or Linux)
# uses correct path separator for os eg '/' on Unix/Linux/macOS and '\' on Windows
# '*' - wildcard character - matches any sequence of characters in a filename. * means ALL
# SO... above code joins home directory path with wildcard character '*' to create a pattern that matches ...
# all files and directories inside the home directory
# called 'portable' wildcard pattern as it adapts to the file path conventions of the os system python script is running on (cross platform)
# Output of code:
# \C:\Users\username\* - windows
# /home/username/* - unix/linux/macOS

# TODO: Use the glob.glob() function to obtain the list of filenames
filenames = glob.glob(pattern)
# declare a variable called filenames and use the glob.glob() function with a path pattern (portable wildcard pattern)
# pattern variable passed to glob.glob() function returns a list of path names that match the pattern in the users home directory
# pattern variable represents all files in the home directory of the current user

# TODO: use os.path.getsize to find each file's size
for filename in filenames:
    size = os.path.getsize(filename)
# os.path.getsize() function returns the size in bytes of the path (file) name passed to it
# loop through each file obtained using glob.glob() function using this function to get their sizes

# TODO: Add a test to only display files that are not zero length
    if size > 0:
        # use a conditonal statement to check if file size is greater than 0

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
        print(os.path.basename(filename))
# os.path.basename() - gets basename of pathname (last part of path) which strips out directory part of file path, leaving only filename
# could do print(filename) instead and it would also print out the file path
#       print(filename)


# ////// Code in full //////

# if sys.platform == 'win32':
#     hdir = os.environ['HOMEPATH']
# else:
#     hdir = os.environ['HOME']
#
# pattern = os.path.join(hdir,'*')
#
# filenames = glob.glob(pattern)
#
# for filename in filenames:
#     size = os.path.getsize(filename)
#     if size > 0:
#         print(os.path.basename(filename))
