#Any Pytest file should start with "test_" or end with "_test"
#pytest method names should start with test
#Any method should be wrapped in method only
#Method Name should have sense for the saperate execution
# in command line execution example - "pytest -k <fliename/methodname> -v -s" OR "py.test -k <fliename/methodname> -v -s"
    # -k stand for method names execution
    # -s stand for log in output
    # -k stand for more info metadata

def test_stringmatch():
    msg = "Hello"
    assert msg == "Hello", "Test Failed becuase string not matched"

def test_creditcard(setup):
    print('creditcard_demo2')

