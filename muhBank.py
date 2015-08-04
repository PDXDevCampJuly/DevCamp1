""""An account file for out Simple Bank."""

class Account:

    def __init__(self, balance, account_type="checking"):
        self.balance = balance
        self.account_type = account_type

    def deposit(self, money):
        self.balance += money
        return self.balance

    def withdrawal(self, money):
        if self.balance < money:
            print("Not enough money in account to withdraw {0}.  Your current balance is {1}"
                .format(money, self.print_balance()))
        else:
            self.balance -= money
        return self.balance

    def check_balance(self):
        return self.balance

    def print_balance(self):
        return '${:,.2f}'.format(self.balance)

    def interest(self, percentage):
        self.balance *= percentage


class Person:
    """ A class that tracks Persons in our bank. """

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.accounts = {}

    def open_account(self, initial_balance, account_name, account_type="checking"):
        new_account = Account(initial_balance, account_type)
        self.accounts[account_name] = new_account

    def deposit(self, money, account_name):
        new_balance = self.accounts[account_name].deposit(money)
        print(" Your new balance is >>", new_balance)


    def withdrawal(self, money, account_name):
        new_balance = self.accounts[account_name].withdrawal(money)
        print(" Your new balance is >>", new_balance)

    def close_account(self, account_name):
        del self.accounts[account_name]

    def show_accounts(self):
        """Display on the screen all of the user's account info. """
        print("Accounts >>> Balance")
        print("______________________________")
        for k,v in self.accounts.items():
            print(k, ">>>", v.print_balance())
        print("\n\n\n")

# class Bank:
#     def __init__(self):
#         self.customers = {}
#         self.savings_interest = 1.07
#
#     def new_customer(self, first_name, last_name, email):
#         new_customer = Person(first_name, last_name, email)
#         customers[email] = new_customer
#
#     def remove_customer(self, email):
#         pass
#
#     def show_customer_info(self, email):
#         pass
#
#     def customer_deposit(self, email, money, account_name):
#         pass
#
#     def customer_withdrawal(self, email, money, account_name):
#         pass
#
#     def make_customer_account(self, email, money, account_name):
#         pass
#
#     def remove_customer_account(self, email, money, account_name):
#         pass



test = Person("Summer", "Bryant", "s.lynbryant@gmail.com")
print(test.first_name)
print(test.last_name)
print(test.email)
test.open_account(65, "New laptop account")
print(test.accounts["New laptop account"])
test.deposit(1500, "New laptop account")
test.withdrawal(350, "New laptop account")
# test.close_account("New laptop account")
# print("Account is closed")
test.show_accounts()

#
# test = Account(100, "Summer")
# print(test.print_balance())
# test.deposit(50)
# print(test.print_balance())
# test.withdrawal(100)
# print(test.print_balance())
# test.interest(2.04)
# print(test.print_balance())
