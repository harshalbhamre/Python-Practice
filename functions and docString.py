# a = 9
# b = 8
# c = sum((a,b))
# print(c)

def func1 (a,b):
    """this is a doc String""" #this is a docString
    average = (a+b)/2
    return average

v = func1(10,15)
print(v)
print(func1.__doc__)  # this function returns the docstring

