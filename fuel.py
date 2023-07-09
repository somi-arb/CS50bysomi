while True:
    fuel = input("FRACTION : ")
    try:
        x, y =fuel.split("/")
        x_ = int(x)
        y_ = int(y)
        f = x_ / y_
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
p = f*100
if p<=1:
    print("E")
elif p>=99:
    print("F")
else:
    print(p,"%")