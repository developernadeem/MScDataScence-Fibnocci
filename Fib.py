def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


# reads the input number
def start():
    s_number = input("Please input a number to calculate a Fibonacci number: ")
    number = int(s_number)
    if number < 0:
        print("You can't do it ")
    else:
        print(fib(number))
        start()


start()
