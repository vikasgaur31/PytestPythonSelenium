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
#Fixtures are used as setup and tear down methods for the test cases - conftest file to generalization
#Fixture and make it available to all test cases
#datadriven and parameterization can be done with return statements in tuple format


import pytest



@pytest.fixture(scope="class")
def setup():
    print('i will be running first')
    yield
    print('i will be running last')

#datadriven and parameterization can be done with return statements in tuple format
@pytest.fixture()
def dataLoad():
    print('User Profile data is being created')
    return["Vikas", "Gaur"]

#datadriven and multiple parameterization can be done with return statements in tuple format
@pytest.fixture(params=[("Chome", "vikas", "SAP"), ("Firefox", "Gaur"), "IE"])
def crossBrowser(request):
    return request.param
