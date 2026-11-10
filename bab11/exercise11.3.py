import pytest

from employee import Employee


@pytest.fixture
def employee():
    return Employee("Andi", "Pratama", 65_000)


def test_give_default_raise(employee):
    employee.give_raise()

    assert employee.salary == 70_000


def test_give_custom_raise(employee):
    employee.give_raise(10_000)

    assert employee.salary == 75_000