def func(*args):
    s = 0
    for n in args:
        s = s + n
    print(s)

func(1,2,3,4)