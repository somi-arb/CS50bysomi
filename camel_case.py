camel_case = input("camel case: ")

for i in camel_case:
    if i.isupper():
        camel_case = camel_case.replace(i, f"_{i.lower()}")

print(camel_case)