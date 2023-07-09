file = input(" enter the file name: ")

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".pdf"):
    print("application/pdf")
else:
    print("application/octet-stream")