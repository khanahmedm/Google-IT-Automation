import csv

with open("Benford.csv") as benford:
  reader = csv.DictReader(benford)
  for row in reader:
    print('{} address has {} invoices.'.format(row["Address"], row["Invoices"]))
