users = [{"username": "admin",
          "password": "admin007",
          "balance": 0.0,
          "role": "admin"}]

def admin_menu():
    print("1. Create new user account")
    print("2. View all users")
    print("3. Update profile")
    print("4. Logout")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1 - 5): ")
    
    if choice == '1':
        create_user()
    elif choice == '2':
        view_all_users()
    elif choice == '3':
        update_profile()
    elif choice == '4':
        logout()
    elif choice == '5':
        exit()
    else:
        print("\nInvalid entry.")

def update_profile():
    while True:
        print(f"Current username: {current_user['username']}")
        print("1. Change Username")
        print("2. Change Password")
        print("3. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            while True:
                new_username = input("Enter new username: ")
                
                current_user["username"] = new_username
                print("Username successfully updated!")
                input("Press Enter to continue...")
                break
        elif choice == "2":
            while True:
                current_password = input("Enter current password: ")
                
                new_password = input("Enter new password: ")
                confirm_password = input("Confirm new password: ")
                
                if new_password != confirm_password:
                    print("Passwords do not match. Please try again.")
                    continue
                
                current_user["password"] = new_password
                print("Password successfully updated!")
                input("Press Enter to continue...")
                break
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter a number between 1-3.")

def create_user():
    while True:
        username = input("Enter new username: ")

        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")

        new_user = {"username": username,
                    "password": password,
                    "balance": 0.0,
                    "role": "user"}

        users.append(new_user)

        print(f"\nSuccessfully created account for {username}")
        return

def view_all_users():
    print(f"{'Username':<20} {'Balance':>15}")
    print("-" * 35)
    
    for user in users:
        print(f"{user['username']:<20} ${user['balance']:>14.2f}")                   

def show_balance():
    print(f"\nYour current balance is: ${balance:.2f}\n")

def transfer():
    while True: 
        recipient_name = input("Enter recipient name: ")

        recipient = None
        for user in users:
            if user["username"] == recipient_name and user !=current_user:
                recipient = user
                break

    while True: 
        amount_input =  input("Enter amount: ")
        try:
            amount = float(amount_input)
            if amount > current_user["balance"]: 
                print("\nInsufficient funds. Please enter another amount.")
                continue
            break
        except ValueError:
            print("\nInvalid input.")

    current_user["balance"] -= amount
    recipient["balance"] += amount

    print(f"\nAmount of ${amount:.2f} has been transferred to {recipient_name}")
    print(f"New balance: ${current_user['balance']:.2f}")
           
def deposit():
  global balance
  try:
     amount = float(input("\nEnter amount to deposit: $"))
     if amount > 0:
        balance += amount
        print(f"${amount:.2f} deposited successfully.\n")
     else:
         print("\nPlease enter a positive amount.\n")
  except ValueError:
      print("\nInvalid input. Please enter a numeric value.\n")

def withdraw():
    global balance
    try:
        amount = float(input("\nEnter amount to withdraw: $"))
        if 0 < amount <= balance:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully.\n")
        elif amount > balance:
            print("\nInsufficient funds.\n")
        else:
            print("\nPlease enter a positive amount.\n")
    except ValueError:
        print("\nInvalid input. Please enter a numeric value.\n")

def user_menu():
    global current_user
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Update Profile")
        print("6. Logout")
        print("7. Exit ATM")
        
        choice = input("\nEnter your choice (1-7)")
        
        if choice == "1":
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            transfer()        
        elif choice == '4':
            show_balance()
        elif choice == '5':
            update_profile()
        elif choice == '6':
            logout()
            return
        elif choice == '8':
            exit_atm()
        else:
            print("\nInvalid choice. Please enter a number between 1-5.")
            input("\nPress Enter to continue...")

def user_login():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        
        for user in users:
            if user["username"] == username and user["password"] == password:
                current_user = user
                print(f"\nWelcome, {username}!")
                return True
        
        print("\nInvalid username or password. Please try again.")
        choice = input("Press 'e' to exit or any other key to try again: ")
        if choice == 'e':
            return False

def exit_atm():
    print("\nThank you for using this ATM. Goodbye!")
    
def logout():
    global current_user
    current_user = None
    print("\nYou have been successfully logged out.")    

admin_menu()             
  

