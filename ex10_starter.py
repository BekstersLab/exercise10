# Practice declaring variables and using different types
# 1. Why is this coding concept this way?
# 2. Is there another way to do this?
# 3. What can I build to help me learn this more? (Maybe not want to build with it)

# what has been imported?
import sys, glob, os

# EXERCISE 1a: Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']  # what does this mean
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
# glob.glob returns a list of files that matches rhe path specified in the function argument
# relative path to search all text files
# uses wildcard character * to match all filepath to the current file

files = glob.glob("*.py")
print(files)

# to show all filenames within current directory
print('Inside current directory')
for item in glob.glob("*"):
    print(item)

# TODO: use os.path.getsize to find each file's size
#  os.path.getsize(filepath) is used to get the size of the file

# list of all file paths
file_paths = ['ex10_starter.py', '.gitignore', 'README.md']

# conditional statement for file_path in file_paths:
for file_path in file_paths:
    # we use the os.path.getsize method to find the size of the file
    size = os.path.getsize(file_path)
    # print('Size of files:', file_path, size)
    # print with f string the size of the file on the console
    print(f"Size of '{file_path}':", size)

# TODO: Add a test to only display files that are not zero length
# file_paths = ['ex10_starter.py', '.gitignore', 'README.md']

for file_path in file_paths:
    if os.path.getsize(file_path) != 0:
        print(f'{file_path} is not equal to zero')


# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
# added file path with directory name
filepath = "C:/code/python_homework/exercise10/ex10_starter.py"

basename = os.path.basename(filepath)

print(basename)

# EXERCISE 2 - Python Program that emulates the high-street mechanism for checking a PIN.
# prompt user to enter pin
supplied_pin = int(input("Enter your PIN: "))
# def the correct pin
desired_pin = 2489
# def max attempts
max_attempts = 3
# initialise num of log in attempts
attempts = 0
# write a password number which is hard-coded by me
while attempts < max_attempts:
    incorrect_pin = int(input("Incorrect PIN. Enter your PIN again: "))

if supplied_pin == desired_pin:
    print('PIN successful')

else:
    attempts += 1
    remaining_attempts = max_attempts - attempts
    print(f"{remaining_attempts} attempts left")

if attempts == max_attempts:
    print('3 UNSUCCESSFUL ATTEMPTS. ACCOUNT LOCKED!')


# while supplied_pin != desired_pin:
#     supplied_pin = int(input("Incorrect PIN. Enter your PIN again: "))
#
# if supplied_pin == desired_pin:
#     print('PIN successful!')


# restrict number if attempts by 3 and write message

# restrict the numbers input to four

