x = 0
count = 0

def func_16(var):
    global count
    count += 1
    var += 16
    print(str(var))
    if count < 18:
        func_16(var)

func_16(x)
