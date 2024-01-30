# //////// WHILE LOOP ////////

# EXERCISE 2 - Python Program that emulates the high-street mechanism for checking a PIN.

# def the correct pin
desired_pin = 2489
# def max attempts
max_attempts = 3
# initialise num of log in attempts
attempts = 0

# while loop is used to execute a set of statements as long it is true
# while attempts is less than three from (0-3)
while attempts < max_attempts:
    # input prompts the user to enter pin as long
    # int changes string values into integer and restricts user to only use integer values
    supplied_pin = int(input("Enter your PIN: "))
    # If user input a string = ValueError

    # indented as the condition is a set of statement within a loop
    # condition: if user input a pin that equals to desired pin
    if supplied_pin == desired_pin:
        # print the below string object in console - PIN successful
        print('PIN successful')
        # break t allows you to exit the loop
        break

    # else used to catch the amount of attempts the user has left
    else:
        # increment attempt by the value 1
        # attempts = attempts + 1
        # this increases the amount of the attempts by 1
        attempts += 1
        # to count the amount of attempts user has left
        # everytime a user makes an attempt to input PIN, it takes 1 away from 3 which is the value of max attempts
        remaining_attempts = max_attempts - attempts
        # prints message of the remaining attempts left using f string
        print(f"{remaining_attempts} attempts left")

# conditional statement: if the attempts is equal to max attempts is TRUE
if attempts == max_attempts:
    # display string object to user 
    print('3 UNSUCCESSFUL ATTEMPTS. ACCOUNT LOCKED!')

# //////// FOR LOOP ////////

# declare and initialise the correct PIN
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
