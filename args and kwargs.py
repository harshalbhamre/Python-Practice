# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
#
# function_name_print("Harry", "rohan", "skillf", "Hammad")

def funargs(normal,*args, **kwargs):
    #print(args[0])
    """
    args return values wihtout any syntactical formats of non key value
    e.g. ["Harry"] will be printed just Harry.
    kwargs is the same but for key-value pairs

    :param args:
    :return:
    """
    print(normal) #normal argument/parameter
    for item in args:
        print(item, end=" ")
    for key, value in kwargs.items():
        print(f"\n{key} is a {value}")

nor = "HI this is a demonstration of args and kwargs and this is a normal argument"
har = ("Harry", "rohan", "skillf", "Hammad")
kw = {"Rohan" : "Monitor", "Harry" : "backbencher"}
funargs(nor, *har, **kw)
