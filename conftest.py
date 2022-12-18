import pytest
from src.Account import Account


@pytest.fixture()
def default_account():
    account = Account("Mr.X", 0)
    yield account
    del account
