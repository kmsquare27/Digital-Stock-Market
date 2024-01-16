class User:
    def _init_(self, username, password, full_name, address, companies=None, stock_amounts=None,
                 balance=0, account_number=None, mob_number=None):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.address = address
        self.companies = companies or []
        self.stock_amounts = stock_amounts or []
        self.balance = balance
        self.account_number = account_number
        self.mob_number = mob_number