
"""

2 kinds of fucntions built in

global and local

"""

foo = 1 #global


def func():
    bar = 2 # local
#    print(foo)
    print(globals()) #help you identify all the globals, help debug
    print(locals()) #help you identify local variables - help debug
#    print(bar)

func()

"""
'foo': 1, 'func': <function func at 0x10b3041e0>}
{'bar': 2}

"""