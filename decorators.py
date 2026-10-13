def mydecorator(function):
    def wrapper():
        print("Function before execution")
        function()
        print("Function after execution")
    return wrapper

@mydecorator
def greet():
    print("Hello")

greet()
