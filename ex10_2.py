# //////// WHILE LOOP ////////

# EXERCISE 2 - Python Program that emulates the high-street mechanism for checking a PIN.
# prompt user to enter pin
# def the correct pin
desired_pin = 2489
# def max attempts
max_attempts = 3
# initialise num of log in attempts
attempts = 0
# write a password number which is hard-coded by me
while attempts < max_attempts:
    supplied_pin = int(input("Enter your PIN: "))
    # incorrect_pin = int(input("Incorrect PIN. Enter your PIN again: "))

    if supplied_pin == desired_pin:
        print('PIN successful')
        break

    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"{remaining_attempts} attempts left")

if attempts == max_attempts:
    print('3 UNSUCCESSFUL ATTEMPTS. ACCOUNT LOCKED!')


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