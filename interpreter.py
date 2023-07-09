x, y, z = input ("").split(" ")

if y == "+":
    s = float(x) + float(z)
elif y == "-":
    s = float(x) - float(z)
elif y == "/":
    s = float(x) / float(z)
elif y == "*":
    s = float(x) * float(z)

print(s)