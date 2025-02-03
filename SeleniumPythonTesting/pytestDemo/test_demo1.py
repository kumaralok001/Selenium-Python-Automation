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
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("GoodMorning")