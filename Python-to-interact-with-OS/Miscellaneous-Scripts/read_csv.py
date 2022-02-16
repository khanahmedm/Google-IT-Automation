import csv

f = open("Benford.csv")
csv_f = csv.reader(f)

for i, row in enumerate(csv_f):
  if i == 0:
    pass
  else:
    Digit, BenfordP, Address, Invoices = row
    print('Digit: {}, BenfordP: {}, Address: {}, Invoices: {}'.format(Digit, BenfordP, Address, Invoices))
