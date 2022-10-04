def get_requirements():
    print('''1. Calc home interior cost (without primer).
2. Must use float data types.
3. Must use SQFT_PER_GALLON constant.
4. Must use iteration structure.
5. Format, right align, and round to two decimal places.
6. Create five functions
    a. main()
    b. get_requirements()
    c. estimate_painting_cost()
    d. print_painting_estimate()
    e. print_painting_percentage()''')
    print()

# global variable
SQFT_PER_GALLON = 350.00

def estimate_painting_cost(inter, ppg, sq_rate):
    number_of_gallons = inter / SQFT_PER_GALLON
    paint_cost= number_of_gallons * ppg 
    tot_labor = sq_rate * inter
    total_fee = tot_labor + paint_cost
    return number_of_gallons, paint_cost, tot_labor, total_fee
    



def print_painting_estimate(a, b, e):
    print('Number of Gallons:{0:>13,.2f}'.format(a))
    print('Paint per Gallon:{0:>5}{1:>9,.2f}'.format('$',e))
    print('Labor per Sqft:{0:>7}{1:>9.2f}'.format('$',b))
    
    
def print_painting_percentage(pc, labor, total):
    paint_percent = pc/total
    labor_percent = labor/total
    total_percent = total/total
    print('Cost\t\tAmount\t\tPercentage')
    print('Paint:\t${0:>15,.2f}{1:>15.2%}'.format(pc, paint_percent))
    print('Labor:\t${0:>15,.2f}{1:>15.2%}'.format(labor, labor_percent))
    print('Total:\t${0:>15,.2f}{1:>15.2%}'.format(total, total_percent))


def main():
    
    repeat = 'y'
    while repeat.lower() =='y':
        print()
        total_interior = float(input('Enter total interior sq ft: '))
        ppg_paint = float(input('Enter price per gallon of paint: '))
        paint_hr_rate = float(input('Enter hourly painting rate per sq ft: '))
        print()
        if repeat.lower() == 'y':
            n, p, tl, tt = estimate_painting_cost(total_interior, ppg_paint, paint_hr_rate)
            print('Item\t\t\tAmount ')
            print('Total Sqft:{0:>20,.2f}'.format(total_interior))
            print('Sqft per Gallon:{0:>15,.2f}'.format(SQFT_PER_GALLON))
            print_painting_estimate(n, paint_hr_rate, ppg_paint)
            print()
            print_painting_percentage(p, tl, tt)
            repeat = input('would you like to repeat (y/n): ')
        else:
            break
    print('Goodbye')


if __name__ == "__main__":
    pass