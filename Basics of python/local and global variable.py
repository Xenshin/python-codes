x = 'awesome' # this is a global variable

def myfunc():
    x = 'fantastic' # this is a local variable
    print("python is "+ x)

myfunc()

print("python is " + x)


'''If you want to use the variable inside the function,
outside of the function too, then declare it as global'''

def myfunc2():
    global a #now this can be used in and outside of the function myfunc2
    a = 'amazing'
    print('python is '+a)

myfunc2()
print("python is "+ a)