import math


# Setting out the calculation type the user would like to proceed with
calculation_type = input("""Please enter which option you would like
    
Investment - Calculates the amount of interest you'll earn on your investment
                
Bond - Calculates the amount you'll have to pay on a home loan
                        """)
print()

# Setting the user response to all lower case so it does not matter which caps they use
calculation_type = calculation_type.lower()

# If investment has been selected ask user for the finer details
if calculation_type == "investment":

    
    money_depositing = float(input("How much money are you wanting to invest?\n \t \t \t"))
    print()
    interest_rate = float(input("What is the interest rate?\n \t \t \t"))
    print()
    num_years = int(input("How many years are you planning on investing for?\n \t \t \t"))
    print()
    interest = input("Is the interest simple or compound\n \t \t \t")
    print()
    interest = interest.lower()

# Ask if simple or compound, work out calculations and print statement answering their questions
    

    if interest == "simple":
        
        total_investment = money_depositing *(1 + interest_rate * num_years / 100) # turning into %
        print(f"""
After depositing £{money_depositing} at an interest rate of {interest_rate}% for {num_years} years you will have earned £{total_investment}.""")

    elif interest == "compound":
        total_investment = money_depositing * math.pow((1 + interest_rate / 100),num_years)
        print(f"""
After depositing £{money_depositing} at an interest rate of {interest_rate}% for {num_years} years you will have earned £{total_investment}.""")

# If bond has been selected ask user for finer details
elif calculation_type == "bond":

    house_value = float(input("What is the current value of your house?\n \t \t \t"))
    print()
    interest_rate = float(input("What is the interest rate?\n \t \t \t"))
    print()
    num_months = float(input("How many months until you repay the loan?\n \t \t \t"))
    print()

    interest_rate = interest_rate / 100 / 12 # dividing answer by 100 to get percentage and then 12 to make monthly

    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-num_months))

    print("You will repay £{:.2f}".format + repayment) # rounding to 2 decimal places

# Add an error message that asks user to pick again if an incorrect statement has been input 
else:
    print("You have chosen an incorrect option, Please start again")