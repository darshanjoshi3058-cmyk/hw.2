instagram = {}
username = input("Enter username: ")
password = input("Enter password: ")

if username in instagram:
    print("Error: Username already exists!")
else:
    instagram[username] = password
    print("Account created successfully!") 

print(instagram)        