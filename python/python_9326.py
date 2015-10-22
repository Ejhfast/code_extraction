# Using funcarg value in pytest_generate_tests function
def pytest_generate_tests(metafunc):
    params = [("input", "output")]
    metafunc.parametrize(("test_case", "result"), params)
