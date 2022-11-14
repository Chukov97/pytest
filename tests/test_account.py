import pytest
from src.Account import Account


@pytest.mark.smoke
def test_account_create_balance():
    a = Account("Mr.X", 0)
    assert isinstance(a, Account)
    assert a.balance == 0


def test_account_create_name():
    a = Account("Mr.X", 0)
    assert isinstance(a, Account)
    assert a.owner == "Mr.X"
