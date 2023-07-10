import random

def get_level():
    while True:
        level = input("Please enter a level (1, 2, or 3): ")
        if level in ['1', '2', '3']:
            return int(level)

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level: {}".format(level))

def generate_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    return "{} + {} = ".format(x, y), str(x + y)

def get_answer(problem):
    for i in range(3):
        answer = input(problem[0])
        if answer.isdigit() and int(answer) == int(problem[1]):
            print("Correct!")
            return True
        print("EEE")
    print("The correct answer is: {}".format(problem[1]))
    return False

def main():
    level = get_level()
    score = 0
    for i in range(10):
        problem = generate_problem(level)
        if get_answer(problem):
            score += 1
    print("Your score is: {}/10".format(score))

if __name__ == '__main__':
    main()
