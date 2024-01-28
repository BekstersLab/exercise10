# //////// FOR LOOP ////////

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

