def get_requirements():
    print("\n Payroll Calculator")
    print("\nDeveloper: Carson Darrow")
    print('''1. must use float data type for user input.
2. Overtime rate is 1.5 times hourly rate (hours over 40).
3. Holiday rate is 2.0 times hourly.
4. Must format with dollar sign and round to 2 decimal places
5. Create three functions''')

#all calculations
def calculate_payroll(week, holiday, pay):
    week = int(week)
    count = 0
    pay1 = pay
    overtime = pay * 1.5
    holiday_pay = pay * 2.0
    # calculated overtime hours using modulous
    overtime_hours = week%40
    overtime_total = overtime * overtime_hours
    holiday_total = holiday * holiday_pay
    #iterating over individual hours 40 times
    for week in range(39):
        pay += pay1
        count+=1
    #total in arithmatic
    total = pay + overtime_total + holiday_total
    print()
    #print statement with all values
    print(f'''Base:\t\t ${pay:.2f}
Overtime:\t ${overtime_total:.2f}
Holiday:\t ${holiday_total:.2f}
Gross:\t\t ${total:.2f}''')

    
def main():
    get_requirements()
    print()
    weeklyhrs = float(input('Enter hours worked: '))
    holidayhrs = float(input('Enter holiday hours worked: '))
    payhr = float(input('Enter hourly pay rate: '))
    calculate_payroll(weeklyhrs, holidayhrs, payhr)
    
if __name__ == "__main__":
    pass


    