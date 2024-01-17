from UserManager import UserManager
from PortfolioManager import PortfolioManager
from CompanyManager import CompanyManager

class BuyManager:
    @staticmethod
    def buy_stocks(user_manager, portfolio_manager):
        username = input("Enter your username: ")

        user = user_manager.get_user(username.strip())
        if user is None:
            print("User not found. Please register first or enter a valid username.")
            return

        company_name = input("Enter Company Name: ")
        num_shares = int(input("Enter Number of Stock: "))

        company_price = CompanyManager.get_stock_price(company_name.strip())
        if company_price == 0:
            print("Company not found or stock price not available.")
            return

        total_cost = company_price * num_shares

        payment_method = input("Choose payment method (bank/bkash): ").lower()

        if payment_method not in ['bank', 'bkash']:
            print("Invalid payment method. Please choose either 'bank' or 'bkash'.")
            return

        confirmation = input(
            f"Are you sure you want to buy {num_shares} shares of {company_name} for {total_cost} BDT? (yes/no): ").lower()

        if confirmation == 'yes':
            if total_cost > user['balance']:
                print("Insufficient funds. Cannot complete the purchase.")
            else:
                portfolio_manager.add_stocks(user, company_name, num_shares, total_cost)
                print(f"Successfully bought {num_shares} stocks of {company_name}.")
                # Update the total stock quantity in company details
                CompanyManager.update_stock_quantity_for_buy(company_name, num_shares)
        else:
            print("Purchase canceled.")

# class SellManager:
#     @staticmethod
#     def sell_stocks(user_manager, portfolio_manager):
#         username = input("Enter your username: ")
#
#         user = user_manager.get_user(username.strip())
#         if user is None:
#             print("User not found. Please register first or enter a valid username.")
#             return
#
#         company_name = input("Enter Company Name to sell stocks: ")
#         if company_name not in user['companies']:
#             print(f"You don't own stocks of {company_name}.")
#             return
#
#         num_shares_owned = user['stock_amounts'][user['companies'].index(company_name)]
#         num_shares_to_sell = int(input(f"Enter the number of shares you want to sell (max {num_shares_owned}): "))
#
#         if num_shares_to_sell <= 0 or num_shares_to_sell > num_shares_owned:
#             print("Invalid number of shares to sell.")
#             return
#
#         company_price = CompanyManager.get_stock_price(company_name.strip())
#         if company_price == 0:
#             print("Company not found or stock price not available.")
#             return
#
#         total_earnings = company_price * num_shares_to_sell
#
#         payment_method = input("Choose payment method (bank/bkash): ").lower()
#
#         if payment_method not in ['bank', 'bkash']:
#             print("Invalid payment method. Please choose either 'bank' or 'bkash'.")
#             return
#
#         confirmation = input(
#             f"Are you sure you want to sell {num_shares_to_sell} shares of {company_name} for {total_earnings} BDT? (yes/no): ").lower()
#
#         if confirmation == 'yes':
#             portfolio_manager.remove_stocks(user, company_name, num_shares_to_sell, total_earnings)
#             print(f"Successfully sold {num_shares_to_sell} stocks of {company_name}.")
#         else:
#             print("Sale canceled.")
#
if __name__ == "__main__":
    market = DigitalStockMarket()
    while True:
        market.display_menu()
        choice = input("Enter your choice: ")
        market.handle_choice(choice)