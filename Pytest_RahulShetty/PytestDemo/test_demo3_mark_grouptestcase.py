#Any Pytest file should start with "test_" or end with "_test"
#pytest method names should start with test
#Any method should be wrapped in method only
#Method Name should have sense for the saperate execution
# in command line execution example - "pytest -k <fliename/methodname> -v -s" OR "py.test -k <fliename/methodname> -v -s"
    # -k stand for method names execution
    # -s stand for log in output
    # -k stand for more info metadata
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#you want to run the test but you dont want to publish into the result - @pytest.mark.xfail

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_stringmatch(setup):
    msg = "Hello"
    assert msg == "Hello", "Test Failed becuase string not matched"

@pytest.mark.xfail
def test_creditcard():
    print('creditcard_demo3')
