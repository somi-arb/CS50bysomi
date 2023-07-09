def main():
    time = input(" what time is it?: ")
    tt = convert(time)
    if tt >= 7 and tt <= 8:
        print("it's breakfast time !!")
    elif tt >= 12 and tt <= 13:
        print("it's lunch time !!")
    elif tt >= 18 and tt <= 19:
        print("it's Dinner time !!")
    else:
        print("")
def convert(time):
    if "a.m" in time and "p.m" in time :
        hours, minutes, pm_am = time.split(" ")
        hours, minutes = hours, minutes. split(":")
        if pm_am == "pm" and int(hours) != 12:
            hours = int(hours) + 12
    else:
        h , m = time.split(":")
        h = float(h) + (float(m)/60)
    return h

if __name__ == "__main__":
    main()