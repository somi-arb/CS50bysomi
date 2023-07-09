import csv
import sys

header = ["first name", "last name", "house"]

if len(sys.argv) == 3:
    if sys.argv[1][-3:] == "csv":
        try:
            with open(sys.argv[1]) as file:
                data = []
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        name = row[0]
                        house = row[1]
                        
                        name = name.strip('"')
                        name_parts = name.split(", ")
                        
                        if len(name_parts) == 2:
                            first_name, last_name = name_parts
                        else:
                            continue
                        
                        student = [first_name, last_name, house]
                        data.append(student)
                    else:
                        print('Invalid row:', row)
            
            data.insert(0, header)
            
            with open(sys.argv[2], 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(data)
        
        except FileNotFoundError:
            sys.exit('Could not read', sys.argv[1])
    
    else:
        sys.exit('Invalid input file format. Must be a CSV file.')
        
elif len(sys.argv) < 3:
    sys.exit('Too few arguments.')
    
elif len(sys.argv) > 3:
    sys.exit('Too many arguments.')
