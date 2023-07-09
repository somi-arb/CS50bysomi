txt = input("input: ")
print("output: ", end="")

for letter in txt:
    if not letter in  ['a', 'e', 'i', 'o', 'u']:
        print(letter, end="")

print()