import sys

if len(sys.argv) == 2:
    if sys.argv[1][-2:] == "py":
        try:
            with open(sys.argv[1]) as file:
                lines = 0
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip() != ' ':
                        lines +=1
                print(lines)
        except FileNotFoundError:
            sys.exit('file not found')
    elif sys.argv[1][-2:] != "py":
        sys.exit('not a py file')
elif len(sys.argv) <2:
            sys.exit('too few arg')
elif len(sys.argv) >2:
            sys.exit('too many arg')

    
