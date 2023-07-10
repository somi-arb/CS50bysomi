def main():
    num = input('fraction: ')
    percentage = convert(num)
    print(gauge(percentage))


def convert(num):
    while True:
        index = num.find('/')
        try:
            x = int(num[:index])
            y = int(num[index+1:])
            fraction = x / y
            if x>y:
                num = input('fraction')
                continue
            else:
                percentage = int(fraction*100)
                return percentage
            
        except(ValueError, ZeroDivisionError):
            continue


def gauge(percentage):
    if percentage >= 99:
        return 'f'
    elif percentage < 10:
        return 'e'
    else:
        return str(f'{percentage}%')


if __name__ == "__main__":
    main()