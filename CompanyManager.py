from UserManager import UserManager

class CompanyManager:
    userManager = UserManager('Username.txt')  # You might need to adjust this based on your file structure

    @staticmethod
    def view_company_list():
        try:
            with open('Company List.txt', 'r') as file:
                companies_data = file.read().split('\n\n')
                for idx, company_data in enumerate(companies_data, start=1):
                    company_lines = company_data.split('\n')
                    if len(company_lines) >= 2:
                        company_name = company_lines[0]
                        industry = company_lines[1]
                        print(f"{idx}. {company_name}, {industry}")
                        print('-' * 30)
                    else:
                        print(f"Error: Malformed company data at index {idx}")
        except FileNotFoundError:
            print("Error: 'Company List.txt' file not found. Please create the file with company details.")

    @staticmethod
    def view_company_details():
        try:
            with open('Company Details.txt', 'r') as file:
                companies_data = file.read().split('\n\n')
                company_names = [company_data.split('\n')[0] for company_data in companies_data]
                print("Available Companies:")
                for idx, company_name in enumerate(company_names, 1):
                    print(f"{idx}. {company_name}")
                while True:
                    choice = input("Enter the number of the company you want to view, or '#' to go back: ")
                    if choice.lower() == '#':
                        break
                    try:
                        choice = int(choice)
                        if 1 <= choice <= len(company_names):
                            chosen_company_data = companies_data[choice - 1]
                            print(chosen_company_data)
                            print('-' * 30)
                        else:
                            print("Invalid choice. Please try again.")
                    except ValueError:
                        print("Invalid choice. Please enter a number.")
        except FileNotFoundError:
            print("Error: 'Company Details.txt' file not found. Please create the file with company details.")

    @staticmethod
    def get_stock_price(company_name):
        # Add logic to retrieve the stock price for the given company
        # You might have a data structure or another method to get this information
        # For example, you could have a dictionary with company prices

        company_prices = {
            'Grameenphone Ltd.': 300,
            'Beximco Pharmaceuticals Ltd.': 200,
            'Square Pharmaceuticals Ltd.': 180,
            'BRAC Bank Ltd.': 80,
            'Robi Axiata Ltd.': 150,
            'Renata Limited': 250,
            'Grameen Bank': 50,
            'IDLC Finance Ltd.': 60,
            'Bangladesh Submarine Cable Company Limited': 70,
            'Eastern Bank Ltd.': 70,
            # ... add more companies as needed
        }

        # Return the stock price for the given company
        return company_prices.get(company_name, 0)

    # @staticmethod
    # def update_stock_quantity_for_buy(company_name, num_stocks):
    #     try:
    #         with open('Company Details.txt', 'r') as file:
    #             companies_data = file.read().split('\n\n')
    #
    #         for idx, company_data in enumerate(companies_data):
    #             if company_name in company_data:
    #                 lines = company_data.split('\n')
    #                 total_stock_line = lines[3].split(':')
    #                 total_stock = int(total_stock_line[1].replace(',', '').strip())
    #
    #                 # Update the total stock quantity
    #                 new_total_stock = max(0, total_stock - num_stocks)
    #                 lines[3] = f"Total Stock: {new_total_stock:,}"
    #
    #                 # Update the company data in the list
    #                 companies_data[idx] = '\n'.join(lines)
    #
    #         # Save the updated company details back to the file
    #         with open('Company Details.txt', 'w') as file:
    #             file.write('\n\n'.join(companies_data))
    #     except FileNotFoundError:
    #         print("Error: 'Company Details.txt' file not found.")
    #
    #     @staticmethod
    #     def update_stock_quantity_for_sell(company_name, num_stocks):
    #         try:
    #             with open('Company Details.txt', 'r') as file:
    #                 companies_data = file.read().split('\n\n')
    #
    #             for idx, company_data in enumerate(companies_data):
    #                 if company_name in company_data:
    #                     lines = company_data.split('\n')
    #                     total_stock_line = lines[3].split(':')
    #                     total_stock = int(total_stock_line[1].replace(',', '').strip())
    #
    #                     # Update the total stock quantity
    #                     new_total_stock = max(0, total_stock + num_stocks)
    #                     lines[3] = f"Total Stock: {new_total_stock:,}"
    #
    #                     # Update the company data in the list
    #                     companies_data[idx] = '\n'.join(lines)
    #
    #             # Save the updated company details back to the file
    #             with open('Company Details.txt', 'w') as file:
    #                 file.write('\n\n'.join(companies_data))
    #         except FileNotFoundError:
    #             print("Error: 'Company Details.txt' file not found.")
    #

    @staticmethod
    def update_stock_quantity_for_buy(company_name, num_stocks):
        try:
            with open('Company Details.txt', 'r') as file:
                companies_data = file.read().split('\n\n')

            for idx, company_data in enumerate(companies_data):
                if company_name in company_data:
                    lines = company_data.split('\n')
                    total_stock_line = lines[3].split(':')
                    total_stock = int(total_stock_line[1].replace(',', '').strip())

                    # Update the total stock quantity
                    new_total_stock = max(0, total_stock - num_stocks)
                    lines[3] = f"Total Stock: {new_total_stock:,}"

                    # Update the company data in the list
                    companies_data[idx] = '\n'.join(lines)

            # Save the updated company details back to the file
            with open('Company Details.txt', 'w') as file:
                file.write('\n\n'.join(companies_data))
        except FileNotFoundError:
            print("Error: 'Company Details.txt' file not found.")

    @staticmethod
    def update_stock_quantity_for_sell(company_name, num_stocks):
        try:
            with open('Company Details.txt', 'r') as file:
                companies_data = file.read().split('\n\n')

            for idx, company_data in enumerate(companies_data):
                if company_name in company_data:
                    lines = company_data.split('\n')
                    total_stock_line = lines[3].split(':')
                    total_stock = int(total_stock_line[1].replace(',', '').strip())

                    # Update the total stock quantity
                    new_total_stock = max(0, total_stock + num_stocks)
                    lines[3] = f"Total Stock: {new_total_stock:,}"

                    # Update the company data in the list
                    companies_data[idx] = '\n'.join(lines)

            # Save the updated company details back to the file
            with open('Company Details.txt', 'w') as file:
                file.write('\n\n'.join(companies_data))
        except FileNotFoundError:
            print("Error: 'Company Details.txt' file not found.")