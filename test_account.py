from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    # test_init
    # -0.5pts: Missing test to check account balance
    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        # negative
        assert self.a1.deposit(-2.55) is False
        assert self.a1.get_balance() == 0

        # zero
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        # positive
        assert self.a1.deposit(2.55) is True
        assert self.a1.get_balance() == 2.55

    def test_withdraw(self):
        # negative
        assert self.a1.withdraw(-2.5) is False
        assert self.a1.get_balance() == 0

        # zero
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0

        # positive invalid
        assert self.a1.withdraw(20) is False
        assert self.a1.get_balance() == 0

        # deposit amount
        assert self.a1.deposit(100) is True
        assert self.a1.get_balance() == 100

        # positive valid
        assert self.a1.withdraw(20) is True
        assert self.a1.get_balance() == 80
