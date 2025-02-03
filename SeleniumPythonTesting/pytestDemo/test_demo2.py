#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
# Any code should be wrapped in method only
#Method name should have sense
#-k stands for method names execution, -s logs in output and -v stands for more info metadata
#we can run specific file with py.test <filename>
#we can mark (tag) tests @pytest.mark.<name> and then rum with -m <name>
#we can skip tests with @pytest.mark.skip
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"