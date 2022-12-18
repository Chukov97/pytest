import pytest


@pytest.mark.smoke
def test_account_create_balance(default_account):
    assert default_account.balance == 0


def test_account_create_name(default_account):
    assert default_account.owner == "Mr.X"
