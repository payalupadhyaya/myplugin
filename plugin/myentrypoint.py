import pexpect

def  entryPoint():
 print("This is the first entry point package")

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="type1",
        help="my option: type1 or type2")

def pytest_funcarg__cmdopt(request):
    return request.config.option.cmdopt

__all__ = [
    'entryPoint'
]


