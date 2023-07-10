import random

while True:
    level = input("level: ")
    try:
        level_ = int(level)
        if level_ > 0:
            break
        else:
            continue
    except ValueError:
        print("invalid ")

n = random.randint(1, level_)
print(n)

while True:
    guess = input("guess: ")
    try:
        guess_ = int(guess)
        if guess_ > 0:
            if guess_ < n:
                print('too small!!')
                break
            elif guess_ > n:
                print('too large!!!')
                break
            else:
                print('just right!')
                break

        else:
            break
    except ValueError:
        print("invalid ")