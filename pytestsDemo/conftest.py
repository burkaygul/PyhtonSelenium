import pytest


@pytest.fixture(scope = "class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Burkay", "Gül", "burkayguel@outlook.com"]

@pytest.fixture(params=[("chrome","Burkay","Guel"), ("Firefox","Fenerbahce"), ("IE", "SS")])
def crossBrowser(request):
     return request.param


