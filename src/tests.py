execfile("bin/activate_this.py", dict(__file__="bin/activate_this.py"))

sys.path.insert(0, os.path.dirname(__file__))

def setup_module(module):
    pass

def teardown_module(module):
    pass
    
"""
patterns
def pytest_generate_tests(metafunc):
    if '<varname>' in metafunc.funcargnames:
        metafunc.addcall(funcargs={'<varname>':<val>})

def test_doSomeTest(<varname>):
    assert <varname> == <something>
"""
