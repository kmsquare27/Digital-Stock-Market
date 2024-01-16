from UserManager import UserManager

class PortfolioManager:
    def __init__(self, userManager):
        self.userManager = userManager


    def view_user_portfolio(self):
        print("Viewing User Portfolio...")
        username = input("Enter the username to view the portfolio: ")
        user = self.userManager.get_user(username)

        if user:
            print("\nUser Portfolio:")
            print(f"Username: {username}")
            print(f"Full Name: {user['full_name']}")
            print(f"Address: {user['address']}")
            print(f"Account Number: {user['account_number']}")
            print(f"Bkash Number: {user['mob_number']}")
            print(f"Balance: {user['balance']}")

            if user['companies']:
                print("\nStocks:")
                for company, amount in zip(user['companies'], user['stock_amounts']):
                    print(f"{company}: {amount} shares")
        else:
            print("User not found.")

    def add_stocks(self, user, company_name, num_shares, total_cost):
        # Check if the user already owns stocks of the given company
        if company_name in user['companies']:
            index = user['companies'].index(company_name)
            # Update the existing stock information
            user['stock_amounts'][index] += num_shares
        else:
            # Add new stock information
            user['companies'].append(company_name)
            user['stock_amounts'].append(num_shares)

        # Update user's balance (subtract the total cost of buying stocks)
        user['balance'] -= total_cost

        # Save the updated user data
        self.userManager.save_user_data()

      #  print(f"Successfully added {num_shares} shares of {company_name} to the portfolio.")

    # Inside the PortfolioManager class
    def remove_stocks(self, user, company_name, num_shares_to_sell, total_earnings):
        # Check if the user owns stocks of the given company
        if company_name in user['companies']:
            index = user['companies'].index(company_name)
            # Check if the user has enough shares to sell
            if user['stock_amounts'][index] >= num_shares_to_sell:
                # Update the existing stock information
                user['stock_amounts'][index] -= num_shares_to_sell
                # Update user's balance (add the total earnings from selling stocks)
                user['balance'] += total_earnings

                # If the user has sold all shares of the company, remove it from the portfolio
                if user['stock_amounts'][index] == 0:
                    user['companies'].pop(index)
                    user['stock_amounts'].pop(index)

                # Save the updated user data
                self.userManager.save_user_data()


            else:
                print("Insufficient shares to sell.")
        else:
            print(f"You don't own stocks of {company_name}.")

    # Inside the PortfolioManager class
    def sell_stocks(self, user, company_name, num_shares_to_sell, total_earnings):
        # Check if the user owns stocks of the given company
        if company_name in user['companies']:
            index = user['companies'].index(company_name)
            # Check if the user has enough shares to sell
            if user['stock_amounts'][index] >= num_shares_to_sell:
                # Update the existing stock information
                user['stock_amounts'][index] -= num_shares_to_sell
                # Update user's balance (add the total earnings from selling stocks)
                user['balance'] += total_earnings

                # If the user has sold all shares of the company, remove it from the portfolio
                if user['stock_amounts'][index] == 0:
                    user['companies'].pop(index)
                    user['stock_amounts'].pop(index)

                # Save the updated user data
                self.userManager.save_user_data()


            else:
                print("Insufficient shares to sell.")
        else:
            print(f"You don't own stocks of {company_name}.")