foo = 10;

def sample_function():
    global foo
    foo = 20
    def inner_function():
        foo = 30
        print(foo)
    
    inner_function()
    print(foo)


sample_function()
print(foo)