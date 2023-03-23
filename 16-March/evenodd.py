# Command to copy table data(users2) from postgreSQL and paste in a new csv file(input.csv)
# COPY users2 TO '/Users/jravathu/Desktop/MANOJ_ASSIGNEMNTS/16-March/input.csv' DELIMITER ',' CSV HEADER;

import csv

def create_files(filename):
    with open(filename, 'r') as ip_file:
        reader = csv.reader(ip_file)
        with open('even.csv', 'w', newline='') as op_file_even:
            with open('odd.csv', 'w', newline='') as op_file_odd:
                writer_even = csv.writer(op_file_even)
                writer_odd = csv.writer(op_file_odd)
                for row in reader:
                    if row[0].isdigit()==False: 
                        continue
                    else:
                        if int(row[0])%2==0:
                            writer_even.writerow(row)
                        else:
                            writer_odd.writerow(row)

create_files('input.csv')