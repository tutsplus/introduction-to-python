bill_total = input('The bill total: ')
tax_percentage = input('The tax percentage: ')
tip_percentage = input('The tip percentage: ')

bill_with_tax = float(bill_total) + (float(tax_percentage) / 100)*float(bill_total)

tip = float(bill_total) * (float(tip_percentage) / 100)

total = bill_with_tax + tip

print('The calculated tip is {0:.2f}'.format(tip))
print('The total amount due is {0:.2f}'.format(total))