#Any Pytest file should start with "test_" or end with "_test"
#pytest method names should start with test
#Any method should be wrapped in method only
#Method Name should have sense for the saperate execution
# in command line execution example - "pytest -k <fliename/methodname> -v -s" OR "py.test -k <fliename/methodname> -v -s"
    # -k stand for method names execution
    # -s stand for log in output
    # -k stand for more info metadata
import pytest


def test_firstprogram(setup):
    print("test_demo1_Hello")

@pytest.mark.smoke
def test_fstprogramcreditcard(setup):
    print("Good Morning - Credit Card demo1")
