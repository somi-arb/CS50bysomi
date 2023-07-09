import sys
from tabulate import tabulate
import csv

if len(sys.argv) == 2:
    if sys.argv[1][-3:] == "csv":
        try:
            data = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                data = list(reader)
                print(tabulate(data, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit('file not found')
    elif sys.argv[1][-3:] != "csv":
        sys.exit('not a csv file')
elif len(sys.argv) <2:
            sys.exit('too few arg')
elif len(sys.argv) >2:
            sys.exit('too many arg')