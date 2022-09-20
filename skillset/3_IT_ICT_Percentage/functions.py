def get_requirements():
    print("Developer: Carson Darrow")
    print("IT/ICT Student Percentage")
    print("\nProgram Requirements:\n"
         + "1. Find the number of IT/ICT students in class.\n"
         + "2. Must use float data type for user input and calculations\n"
         + "3. Format, right-align numbers and round to two decimal places.\n")

def calculate_it_ict_students_percentage():
       it = 0.0 
       ict = 0.0
       total_students = 0.0
       percent_it = 0.0 
       percent_ict = 0.0

       print("Input:")
       it = int(input("Enter number of IT students: "))
       ict = int(input("Enter number of ICT students: "))


       total_students = it + ict


       percent_it = it/total_students


       percent_ict = ict/total_students


       print("\nOutput:")
       print("{0:17} {1:>5.2f}".format("Total Students: " , total_students))
       print("{0:17} {1:>5.2%}".format("IT Students: " , percent_it))
       print("{0:17} {1:>5.2%}".format("ICT Students: " , percent_ict))


