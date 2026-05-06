userName = "admin"
userPassword = "admin123"
maxChance = 3

def login():
    currChance = 0
    
    while currChance < maxChance:
        user = input("Enter username: ").strip()
        password = input("Enter password: ")
        
        if user == userName and password == userPassword:
            return True
        else:
            currChance += 1
            print("Invalid credentials")
    
    return False

print(login())




