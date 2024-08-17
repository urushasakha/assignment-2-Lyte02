import json
import os

def read_file():
    if os.path.exists('UserDetails.json'):
        with open('UserDetails.json','r') as file:
            try:
                file_data= json.load(file)
                return file_data
            except Exception as e:
                file_data={}
                return file_data
                print("File not found.")
    else:
        file_data={}
        return file_data



def user_management():
    while True:
        print("1. Sign up")
        print("2. Login ")
        print("3. Exit")

        choice = input("Enter 1,2 or 3: ")

        if(choice=="1"):
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            mobile_number = input("Enter your mobile number : ")

            file_details = read_file()
            print(file_details)
            if username in file_details:
                print("Username already exists.")
            
            else:
                file_details[username] = {
                    'UserName': username,
                    'Password': password ,
                    'MobileNumber': mobile_number
                }

                with open ('UserDetails.json','w') as file:
                    json.dump(file_details,file)
                
                print('Signup successful.')
        
        elif(choice=='2'):
            username = input('Enter your username : ')
            password = input('Enter your password : ')

            file_data = read_file()

            if(username in file_data and file_data[username]['Password']==password):
                print(f"Welcome , {username} !  ")
                print(f" Your Username : {file_data[username]['UserName']}")
                print(f" Your Mobile Number : {file_data[username]['MobileNumber']}")
                print("------"*10)
            else:
                print("Incorrect username or password.")
                break
        elif choice == '3':
            print("Program is termnated.")
            break
        else:
            print("Invalid choice")

user= user_management()