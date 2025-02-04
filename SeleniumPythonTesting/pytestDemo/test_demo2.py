#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
# Any code should be wrapped in method only
#Method name should have sense
#-k stands for method names execution, -s logs in output and -v stands for more info metadata
#we can run specific file with py.test <filename>
#we can mark (tag) tests @pytest.mark.<name> and then rum with -m <name>
#we can skip tests with @pytest.mark.skip
#@pytest.mark.xfail to ignore the execution of method if its fail
#Fixtures are used as set up and tear down methods for test cases - conftest file to generalize
#fixture and make it available to all test cases.
#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end.

import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


# @pytest.fixture()
# def setup():
#     print("I will be executing first")
#
# def test_fixtureDemo(setup):
#     print("I will execute steps in fixtureDemo method")