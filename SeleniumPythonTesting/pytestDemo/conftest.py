import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Alok", "Kumar", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "Alok", "Kumar"), ("Firefox", "Kumar"), ("IE", "SS")])
def crossBrowser(request):
    return request.param

