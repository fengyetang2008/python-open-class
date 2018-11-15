
def foo(obj):
    obj.name = 'foo'
    return obj

@foo        # => bar = foo(bar)
def bar():
    print('bar')
# bar = foo(bar)

print(bar.name)

