import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)
def test_account():
    return BankAccount(100)
x=2

def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150
def test_failed_deposit(start_account):
    with pytest.raises(ValueError):
        start_account.deposit(-35)
    
def test_withdraw(start_account):
    
    start_account.withdraw(50)
    assert start_account.balance==50
def test_failed_withdraw(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(1000000)
def test_failed_withdraw_neg(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(-50)
def test_transfer(start_account,test_account):
    start_account.transfer_to(test_account,50)
    assert test_account.balance==150 and start_account.balance==50
def test_failed_transfer(start_account):
    with pytest.raises(ValueError):
        start_account.transfer_to(x,50)




