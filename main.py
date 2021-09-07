import csv

dict = {1:'Hello', 2: 'Hi', 3:'bye'}

#Task 1 - Write dict to csv file
with open('assignment3.csv', 'w', newline ='') as f:
    w = csv.DictWriter(f, dict.keys())
    w.writeheader()
    w.writerow(dict)

#Task 2 -  Read file back into dict
with open("assignment3.csv", 'r') as f:
    csv_file = csv.DictReader(f)
    for row in csv_file:
        print(row)








