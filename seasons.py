import datetime

def main(age_in_words):
    bday = input('Enter your birthday (YYYY-MM-DD): ')
    age = calc_age_in_min(bday)
    print(age_in_words)

def calc_age_in_min(bday):
    today = datetime.date.today()
    bday_time = datetime.datetime.strptime(bday, "%Y-%m-%d").date()
    age = today - bday_time
    age_min = age.days * 24 * 60
    return age_min

def age_in_min(age_min):
    minutes = age_min % 60
    hours = (age_min // 60) % 24
    days = (age_min // (60 * 24)) % 365
    years = age_min // (60 * 24 * 365)

    age_in_words = []
    if years > 0:
        age_in_words.append(f"{years} year" + ("s" if years > 1 else ""))
    if days > 0:
        age_in_words.append(f"{days} day" + ("s" if days > 1 else ""))
    if hours > 0:
        age_in_words.append(f"{hours} hour" + ("s" if hours > 1 else ""))
    if minutes > 0:
        age_in_words.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))

    if len(age_in_words) == 0:
        age_in_words.append("less than a minute")

    return age_in_words

if __name__ == "__main__":
    import datetime

def main(age_in_words):
    bday = input('Enter your birthday (YYYY-MM-DD): ')
    age = calc_age_in_min(bday)
    print(age_in_words)

def calc_age_in_min(bday):
    today = datetime.date.today()
    bday_time = datetime.datetime.strptime(bday, "%Y-%m-%d").date()
    age = today - bday_time
    age_min = age.days * 24 * 60
    return age_min

def age_in_min(age_min):
    minutes = age_min % 60
    hours = (age_min // 60) % 24
    days = (age_min // (60 * 24)) % 365
    years = age_min // (60 * 24 * 365)

    age_in_words = []
    if years > 0:
        age_in_words.append(f"{years} year" + ("s" if years > 1 else ""))
    if days > 0:
        age_in_words.append(f"{days} day" + ("s" if days > 1 else ""))
    if hours > 0:
        age_in_words.append(f"{hours} hour" + ("s" if hours > 1 else ""))
    if minutes > 0:
        age_in_words.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))

    if len(age_in_words) == 0:
        age_in_words.append("less than a minute")
    else:
        exit()

    return age_in_words

if __name__ == "__main__":
    age_in_words = age_in_min(calc_age_in_min(input('Enter ur bday : ')))
    main(age_in_words)

