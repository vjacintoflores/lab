class Account:
    """
    A class representing a person's bank account.
    """

    def __init__(self, name:str) -> None:
        """
        Method to set default values for each account object.
        :param name: Person's name.
        :param balance: Person's balance.
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount:float) -> bool:
        """
        Method to increment a person's balance by the specified amount input.
        :param amount: how much to increment.
        :return: boolean true if transaction successful, false if transaction not successful.
        """
        if amount > 0:
            self.__account_balance = amount + self.__account_balance
            return True
        else:
            return False


    def withdraw(self, amount:float) -> bool:
        """
        Method to decrement the person's balance by the specified amount input.
        :param amount: how much to decrease from the balance.
        :return: boolean true if transaction successful, false if transaction not successful.
        """
        if (amount < self.__account_balance) and (amount > 0):
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False

    def get_balance(self) -> None:
        """
        Method to access the account balance.
        :return: Account balance.
        """
        return self.__account_balance

    def get_name(self) -> None:
        """
        Method to access th name associated with the account.
        :return: Person's name.
        """
        return self.__account_name