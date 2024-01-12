
import locale as lc

def value():
    future = 0
    for i in range(years * 12):
        future += monthly
        mon_int = future * interest/(12*100)
        future += mon_int
    return future

monthly = float(input("Enter monthly investment: "))
interest = float(input("Enter yearly interest rate: "))
years = int(input("Enter number of years: "))
future_value = value()
lc.setlocale(lc.LC_ALL, 'en-ca')
print('monthly investment\t\t',lc.currency(monthly))
print(f'Interest rate\t\t\t\t{interest}')
print(f'Years\t\t\t\t\t\t{years}')
print('Future value\t\t',lc.currency(future_value, grouping = True))
