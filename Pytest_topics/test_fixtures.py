import pytest
@pytest.fixture()
def setup_list():
    print("\n in fixtures..\n")
    city = ['Toronto', 'Waterloo', 'Kitchener', 'Guelph']
    return city


def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[1] == "Waterloo"
    assert setup_list[::2] == ['Toronto', 'Kitchener', 'Guelph']
