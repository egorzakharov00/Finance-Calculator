# import math library
import math

# Get input option from user
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment   - to calculate the amount of interest you'll earn on interest")
print("bond         - to calculate the amount you'll have to pay on a home loan")

# get input and make lower case
choice = input().lower()

# Check choice and proceed with program

if choice == "investment":
    # Get more user input
    amount = float(input("Enter the amount of money you are depositing:\n"))
    rate = float(input("Enter the interest rate without a '%':\n"))/100
    years = float(input("Enter the number of years you plan on investing for:\n"))
    interest = input("Enter the type of interest you want to earn:\n'simple' or 'compound'\n")
    # Check choice and proceed with program
    # Calculate result and output
    if interest == "simple":
        final_amount = round(amount*(1+rate*years), 2)
        print("The final amount is R"+str(final_amount))
    else:
        final_amount = round(amount*math.pow((1+rate), years), 2)
        print("The final amount is R"+str(final_amount))

elif choice == "bond":
    # Get more user input
    present_value = float(input("Enter the present value of the house:\n"))
    rate = float(input("Enter the interest rate without a '%':\n"))/100
    months = float(input("Enter the number of months you plan to take to repay the bond:\n"))
    # Calculate result and output
    monthly_amount = round((rate*present_value)/(1-(1+rate)**(-months)), 2)
    print("The repayment per month is R" + str(monthly_amount))

# Output error statement if invalid input
else:
    print("Invalid choice")
