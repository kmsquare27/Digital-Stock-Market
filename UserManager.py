from User import User
import bcrypt


class UserManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_user_data()

    # ... rest of the class remains unchanged


    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            return None

    def load_user_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.readlines()
                users = {}
                for line_number, line in enumerate(data, start=1):
                    # Skip empty lines or lines with only whitespace
                    if not line.strip():
                        print(f"Warning: Skipping empty line at line {line_number}.")
                        continue

                    parts = line.strip().split(':')

                    if len(parts) >= 9:
                        (
                            username, password, full_name, address, companies,
                            stock_amounts, balance, account_number, mob_number
                        ) = parts[:9]

                        # Check if stock_amounts is not empty before converting to integers
                        if stock_amounts:
                            stock_amounts = list(map(int, stock_amounts.split(',')))
                        else:
                            stock_amounts = []

                        # print(
                        #     "##################################################################################" + str(
                        #         balance))

                        # Convert balance to float
                        balance = float(balance)

                        users[username] = {
                            'password': password,
                            'full_name': full_name,
                            'address': address,
                            'companies': companies.split(','),
                            'stock_amounts': stock_amounts,
                            'balance': balance,  # Keep the balance as a float
                            'account_number': account_number,
                            'mob_number': mob_number
                        }
                    else:
                        print(f"Error: Malformed user data at line {line_number}. Skipping...")
                return users
        except FileNotFoundError:
            return {}

    def save_user_data(self):
        try:
            with open(self.file_path, 'w') as file:
                for username, user_data in self.users.items():
                    password = user_data['password']
                    full_name = user_data['full_name']
                    address = user_data['address']
                    companies = ','.join(user_data['companies'])
                    stock_amounts = ','.join(map(str, user_data['stock_amounts']))
                    balance = user_data['balance']
                    account_number = user_data['account_number']
                    mob_number = user_data['mob_number']

                    file.write(
                        f"{username}:{password}:{full_name}:{address}:{companies}:{stock_amounts}:{balance}:{account_number}:{mob_number}\n"
                    )
        except Exception as e:
            print(f"Error saving user data: {e}")

    def update_user(self, user):
        # Update the user data
        for username, existing_user in self.users.items():
            if username == user.username:
                self.users[username] = user
                self.save_user_data()
                break

    def register_user(self):
        while True:
            username = input("Enter a new username: ")

            if not username:
                print("Error: Username cannot be empty.")
                continue

            if username in self.users:
                print("Error: This username is already in use. Please choose a different username.")
            else:
                password = input("Enter a new password: ")
                if 6 <= len(password) <= 15 and any(char.isupper() for char in password):
                    full_name = input("Enter your full name: ")
                    address = input("Enter your Address: ")
                    account_number = input("Enter your Account Number: ")
                    mob_number = input("Enter your Mobile Number: ")
                    net_balance = float(input("Enter your Net Balance: "))  # New line

                    # Securely hash the password before storing it
                    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                    user_data = f"{username}:{hashed_password.decode('utf-8')}:{full_name}:{address}:::0:{account_number}:{mob_number}\n"
                    with open(self.file_path, 'a') as file:
                        file.write(user_data)

                    # Display the entered balance in the console
                    print(f"User registered successfully! Net Balance: {net_balance}")

                    self.users[username] = {
                        'password': hashed_password.decode('utf-8'),
                        'full_name': full_name,
                        'address': address,
                        'companies': [],
                        'stock_amounts': [],
                        'balance': net_balance,  # Set the balance to the entered net balance
                        'account_number': account_number,
                        'mob_number': mob_number
                    }
                    break
                else:
                    print("Error: Password must be 6 to 15 characters long and contain at least one capital letter.")

    def update_company_details(self, user, num_shares, company_name, total_cost, is_buy):
        # Update user balance and stock details after buying or selling stocks
        if is_buy:
            # Update user's balance and add the purchased stocks to the portfolio
            user['companies'].append(company_name)
            user['stock_amounts'].append(num_shares)

            # Subtract the total cost from the user's balance
            user['balance'] -= total_cost
        else:
            # Update user's balance and remove the sold stocks from the portfolio
            index = user['companies'].index(company_name)
            user['companies'].pop(index)
            user['stock_amounts'].pop(index)
            # Add the total cost from the user's balance (since it's a sell operation)
            user['balance'] += total_cost

        # Save the updated user data
        self.save_user_data()

    def login(self, username, password):
        if username in self.users:
            stored_password = self.users[username]['password'].encode('utf-8')
            salt = stored_password[:29]  # Extract the first 29 characters as the salt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            if hashed_password == stored_password:
                return True
        return False