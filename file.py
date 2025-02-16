limit = 3
try:
    with open("users.txt", "r") as file:
        usercreds = file.read().splitlines()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission error")

while limit > 0:
    username = input("Enter your username: ")

    if not username:
        print("Username or password cant be empty. Please try again")
        exit()

    password = input("Enter your password: ")
    
    if not password:
        print("Username or password cant be empty. Please try again")
        exit()

    found = False
    for user in usercreds:
        user, passwd = user.split(",")

        if user == username and passwd == password:
            found = True
            break 

    if found == True:
        print("Login Successful!")
        break 
    else:
        limit = limit - 1
        print(f"Incorrect username or password. {limit} attempts remaning.")

    if limit == 0:
        print("Account Locked!")
        exit()
