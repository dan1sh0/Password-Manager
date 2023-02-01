# create a password generator that asks the use the length of the password they would like then it presents a password.
# after, the user will be asked a name to associate the password with then it will be put into a txt file

# libraries needed
import random
import string

master_password = input("Enter Master Password:")
#this will be the create function where it will ask for length and create it using digits and alphabets 
def create():
    name = input('Password Name: ' )
    length = int(input("Length of password?"))
    characters = list((string.ascii_letters + string.digits ))
    random.shuffle(characters)
    passw=[]
    # loop to create a random password
    for i in range(length):
        new=random.choice(characters)
        passw.append(new)
    random.shuffle(passw)
    password = "".join(passw)
    # puts the generated password into the text file
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + password  + "\n")

# function to view the passwords from the text file
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split('|')
            print('Username:', user, '| Password:', passw)

# loop to present questions for what the user wants to do
while True:

    mode = input("Would you like to create or view passwords?(create,view) If not, press q ")
    if mode == "q":
        break

    if mode == "create":
        create()
    elif mode == "view":
        view()
    else:
        print("invalid mode")
        continue
