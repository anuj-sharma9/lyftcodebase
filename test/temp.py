




def foo(n):
    if n > 1:
        for i in range(5):
            foo(n / 4)
        for i in range(n * n):
            print("Hello")
    else:
        print("World")


foo(16)