from UserManager import UserManager
from PortfolioManager import PortfolioManager
from CompanyManager import CompanyManager
from BuyManager import BuyManager
from SellManager import SellManager



class DigitalStockMarket:
    def __init__(self):
        self.UserManager = UserManager('Username.txt')
        self.PortfolioManager = PortfolioManager(self.UserManager)
        # self.stock_transaction_manager = StockTransactionManager(self.UserManager)
        self.BuyManager = BuyManager()
        self.SellManager = SellManager()
    # rest of the class remains unchanged

    def display_menu(self):
        print("\nWELCOME TO DIGITAL STOCK MARKET")
        print("Choose an option:")
        print("1. Register")
        print("2. Login")
        print("3. View Company List")
        print("4. View Company Details")
        print("5. View User Portfolio")
        print("6. Buy Stocks")
        print("7. Sell Stocks")
        print("8. Payment Method")
        print("9. Dynamic Price Generation")
        print("10. Quit")

    def handle_choice(self, choice):
        if choice == '1':
            self.UserManager.register_user()
        elif choice == '2':
            self.login_user()
        elif choice == '3':
            CompanyManager.view_company_list()
        elif choice == '4':
            CompanyManager.view_company_details()
        elif choice == '5':
            self.PortfolioManager.view_user_portfolio()
        elif choice == '6':
          #  self.buy_stocks()
          self.BuyManager.buy_stocks(self.UserManager, self.PortfolioManager)
        elif choice == '7':
          #  self.sell_stocks()
          self.SellManager.sell_stocks(self.UserManager, self.PortfolioManager)
        elif choice == '8':
            # Add your logic for the payment method here
            print("Payment Method")
        elif choice == '9':
            self.dynamic_price_generation()
        elif choice == '10':
            print("Exiting... Thank you!\n")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if self.UserManager.login(username, password):
            print("Login successful!")
        else:
            print("Username or password does not match.")

    # def buy_stocks(self):
    #     # Ask the user for details
    #     username = input("Enter your username: ")
    #
    #     # Check if the user is registered
    #     user = self.UserManager.get_user(username.strip())
    #     if user is None:
    #         print("User not found. Please register first.Or enter a valid user name.")
    #         return
    #
    #     company_name = input("Enter Company Name: ")
    #     num_shares = int(input("Enter Number of Stock: "))
    #
    #     # Retrieve company information
    #     company_price = CompanyManager.get_stock_price(company_name.strip())
    #     if company_price == 0:
    #         print("Company not found or stock price not available.")
    #         return
    #
    #     total_cost = company_price * num_shares
    #
    #     # Choose payment method
    #     payment_method = input("Choose payment method (bank/bkash): ").lower()
    #
    #     if payment_method not in ['bank', 'bkash']:
    #         print("Invalid payment method. Please choose either 'bank' or 'bkash'.")
    #         return
    #
    #     # Confirm the user's intention to buy stocks
    #     confirmation = input(
    #         f"Are you sure you want to buy {num_shares} shares of {company_name} for {total_cost} BDT? (yes/no): ").lower()
    #
    #     if confirmation == 'yes':
    #         if total_cost > user['balance']:
    #             print("Insufficient funds. Cannot complete the purchase.")
    #         else:
    #             # Add the purchased stocks to the user's portfolio
    #             self.PortfolioManager.add_stocks(user, company_name, num_shares, total_cost)
    #
    #             # Update the company details
    #             #self.UserManager.update_company_details(user, num_shares, company_name, total_cost, is_buy=True)
    #             print(f"Successfully bought {num_shares} stocks of {company_name}.")
    #             # Save the updated user data
    #             # self.UserManager.save_user_data()
    #     else:
    #         print("Purchase canceled.")
    #
    # # Other methods go here
    #
    # # Inside the DigitalStockMarket class
    # def sell_stocks(self):
    #     # Ask the user for details
    #     username = input("Enter your username: ")
    #
    #     # Check if the user is registered
    #     user = self.UserManager.get_user(username.strip())
    #     if user is None:
    #         print("User not found. Please register first or enter a valid username.")
    #         return
    #
    #     # Get the details of the stocks the user wants to sell
    #     company_name = input("Enter Company Name to sell stocks: ")
    #     if company_name not in user['companies']:
    #         print(f"You don't own stocks of {company_name}.")
    #         return
    #
    #     num_shares_owned = user['stock_amounts'][user['companies'].index(company_name)]
    #     num_shares_to_sell = int(input(f"Enter the number of shares you want to sell (max {num_shares_owned}): "))
    #
    #     if num_shares_to_sell <= 0 or num_shares_to_sell > num_shares_owned:
    #         print("Invalid number of shares to sell.")
    #         return
    #
    #     # Retrieve company information
    #     company_price = CompanyManager.get_stock_price(company_name.strip())
    #     if company_price == 0:
    #         print("Company not found or stock price not available.")
    #         return
    #
    #     total_earnings = company_price * num_shares_to_sell
    #
    #     payment_method = input("Choose payment method (bank/bkash): ").lower()
    #
    #     if payment_method not in ['bank', 'bkash']:
    #         print("Invalid payment method. Please choose either 'bank' or 'bkash'.")
    #         return
    #
    #     # Confirm the user's intention to sell stocks
    #     confirmation = input(
    #         f"Are you sure you want to sell {num_shares_to_sell} shares of {company_name} for {total_earnings} BDT? (yes/no): ").lower()
    #
    #     if confirmation == 'yes':
    #         # Remove the sold stocks from the user's portfolio
    #         self.PortfolioManager.remove_stocks(user, company_name, num_shares_to_sell, total_earnings)
    #
    #         # Update the company details
    #       #  self.UserManager.update_company_details(user, num_shares_to_sell, company_name, total_earnings,
    #                                    #              is_buy=False)
    #         print(f"Successfully sold {num_shares_to_sell} stocks of {company_name}.")
    #         # Save the updated user data
    #         # self.UserManager.save_user_data()
    #     else:
    #         print("Sale canceled.")
    #

if __name__ == "__main__":
    market = DigitalStockMarket()
    while True:
        market.display_menu()
        choice = input("Enter your choice: ")
        market.handle_choice(choice)
