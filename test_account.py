import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'

    def test_deposit(self):
        # negative, zero, positive
        assert self.a1.deposit(-2.55) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(2.55) is True
        assert self.a1.get_balance() == 2.55

    def test_withdraw(self):
        # negative, zero, positive invalid, positive valid
        assert self.a1.withdraw(-2.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() ==0

        assert self.a1.withdraw(20) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(100) is True
        assert self.a1.get_balance() == 100

        assert self.a1.withdraw(20) is True
        assert self.a1.get_balance() == 80

