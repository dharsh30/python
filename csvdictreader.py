import csv
with open('Salary_Data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       print(row)