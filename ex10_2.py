# //////// FOR LOOP ////////

# EXERCISE 2 - Python Program that emulates the high-street mechanism for checking a PIN.
# prompt user to enter pin
desired_pin = 2489
# def max attempts
max_attempts = 3
# initialise num of log in attempts
attempts = 0
supplied_pin = int(input("Enter your PIN: "))
# def the correct pin


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


# //////// FOR LOOP ////////

# declare and initialise the correct PIN number
correct_pin = 1984
# declare and initialise attempt count to 0
count = 0

# start a loop that will run up to 3 times
for i in range(3):
    # input prompts user to input PIN number, int() converts the string input to an integer
    supplied_pin = int(input("Enter your PIN: "))
    # increment the attempt counter by 1. Could be written as count = count + 1
    # this will increase by one each time the loop is repeated
    count += 1
    # use equality operator to check if entered PIN matches correct_pin
    if supplied_pin == correct_pin:
        # print message if correct, giving the attempt number, break exits the loop
        print(f"Correct - attempt {count} of 3")
        break
    # != means not equals, if PIN entered does not match correct_pin...
    if supplied_pin != correct_pin:
        # print message if PIN doesn't match giving attempt number
        print(f"Incorrect - attempt {count} of 3")
        # repeat the for loop again, another 2 times maximum (as count of 3 specified).
else:
    # for loop ends after 3 loops with print message giving attempt number which will match number in range() function
    print(f"You've exceeded {count} attempts. Please speak to your branch manager!")

# # //////// WHILE LOOP ////////
#
# # declare and initialise the correct pin number
# correct_pin = 1984
# # declare and initialise count as 0
# count = 0
#
# # use a while loop with and if/else conditional statement
# # while loops normally used when number of iterations unknown, this time it is known to be 3, but can still be used
# # use <=2 rather than 3 as starting from 0, therefore 0, 1, 2 is three times
# while count <=2:
#     # use the input function to request user to enter a string
#     # int() function converts the string to an integer (whole number)
#     # the value is placed in the supplied_pin variable
#     supplied_pin = int(input("Enter your PIN: "))
#     # start of if/else statement
#     # the equality operator checks if the contents of supplied_pin variable exactly matches the contents of correct_pin variable
#     if supplied_pin == correct_pin:
#         # if it is a match then this print statement runs
#         # uses an f-string to minimise untidy concatenation
#         # count + 1 will return 1 the first time the loop is run. If repeated it will increase by 1 to return 2 and then 3
#         print(f"Correct - attempt {count + 1} of 3")
#         # if supplied_pin and correct_pin contents match then the loop breaks (exits)
#         break
#     # if supplied_pin and correct_pin contents do not match after 3 iterations then this code runs
#     else:
#         # the print statement declares that the pin is incorrect and gives the number of attempts either 1, 2 or 3
#         print(f"Incorrect - attempt {count + 1} of 3")
#         #
#         count += 1
#         # use plus-equal operator, same as count = count + 1
