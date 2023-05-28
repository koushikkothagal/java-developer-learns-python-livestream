def test_function(arg1, /, arg2, *, arg3, name='Foo'):
    print(arg1)
    print(arg2)
    print(arg3)
    print(name)

# test_function(arg1='1', arg2='2', arg3='3')


def test_function_2(arg1, /, **kwd):
    print(arg1)
    print(kwd)

# test_function_2('1', arg1='2')

def test_unpack(arg1: 'foo', arg2: 1 + 1, arg3) -> 100*2:
    """Prints the args passed in.
    Just prints it.
    """
    print(arg1)
    print(arg2)
    print(arg3)

test_unpack(*range(1, 4))
print(test_unpack.__annotations__)
