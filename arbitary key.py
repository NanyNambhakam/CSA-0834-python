def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'SIMATS')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key,value))

myFun(first= 'Geeks',mid='for',last='geeks')
