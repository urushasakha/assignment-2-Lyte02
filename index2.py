'''WAP that first gives 2 options: 
Sign up
Sign in

when 1 is pressed user needs to provide following information 
Username, 2. Password, 3. Mobile number
All this information is saved in a file everytime a new user signs up the same file is updated 
(hint Append over the same file)

when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 


Do it using json files, save everything to json and load from json'''


import json     #importing json and os
import os

def sign_up():                              
    username = input("Enter username: ")
    password = input("Enter password: ")
    mobile_number = input("Enter mobile number: ")

    user_data = {"username": username, "password": password, "mobile_number": mobile_number}

    try:
        with open("user_database.json", "r") as f:
            database = json.load(f)
    except FileNotFoundError:
        database = []

    database.append(user_data)

    with open("user_database.json", "w") as f:
        json.dump(database, f, indent=4)

    print("Sign up successful!")

def sign_in():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("user_database.json", "r") as f:
            database = json.load(f)
    except FileNotFoundError:
        print("No user database found. Please sign up first.")
        return

    for user in database:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome to the device! Your mobile number is {user['mobile_number']}")
            return
        elif user["username"] != username and user["password"] == password:
            print("Incorrect username.")                #users can try agian of only username is incorrect                         
        
        else:
            print("Incorrect credentials. Terminating program.") #no chance straight termination
            exit()

def main():
    while True:
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit:") #i added extra exit step to terminate the program without having to give false creditentials to terminate
        choice = input("Enter your choice: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            os._exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()