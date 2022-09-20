SQ_FEET_PER_ACRE = 43560

def get_requirements():
    print("Developer: Carson Darrow")
    print("Square Feet to Acres")
    print("\nProgram Requirements:\n"
         + "1. Research number of square feet to acre of land.\n"
         + "2. Must use float data type for user input and calculations\n"
         + "3. Format and round conversion to two decimal places.\n")

def calculate_sqft_to_acre():
       tract_size = 0.0 
       acres = 0.0
       
       
       print("input:")
       tract_size = float(input("Enter square feet: "))
       acres = tract_size / SQ_FEET_PER_ACRE


       print("\nOutput:")
       print("{0:,.2f} {1} {2:,.2f} {3}".format(
           tract_size, "square feet =", acres, "acres"))


