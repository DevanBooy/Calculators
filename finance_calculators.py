import math 

print("Welcome to your Financial Calculator! ")

print() #print empty line for space

print("Choose either 'Investment' or 'Bond' from the menu below to proceed: ")


# User input 
financial_calc = (input("""    
                             Investment - to calculate the amount of interest you'll earn on interest 
                             or 
                             Bond - to calculate the amount you'll have to pay on a home loan: """)).casefold()

print() #print empty line for space

#If user inputs investment

if financial_calc == "investment":
    P = float(input("Please enter your investment amount: R "))
    R = float(input("Please enter your interest rate as a percentage: "))
    N = int(input("Please enter the number of years you plan on investing for: "))
    interest = input("Please select whether you want 'Simple' or 'Compound' interest: ").casefold()
    
    print()    
         
    if interest == "simple":
        simple_interest = (P * N * R)/100                        #Simple interest formula
        print(f"Your intial investment of R{float(P)} after {int(N)} years at {int(R)} % p.a. on Simple interest would be: R{round(simple_interest, 2)} ")
    else:
        compound_interest = P* (math.pow((1 + R / 100), N))      #Compound interest formula
        print(f"Your intial investment of R{float(P)} after {int(N)} years at {int(R)} % p.a. on Compoud interest would be: R{round(compound_interest, 2)} ")     

#If user inputs bond
    
elif financial_calc == "bond":
    L = float(input("Please present the current value of the house: R"))
    rate = float(input("Monthly interest rate: "))/100
    months = int(input("Number of months over which the bond will be repaid: "))
    
    loan_repayment = (rate/12) * (1/(1-(1+rate/12)**(-months)))*L  #Bond repayment formula
    print(f"""
          Present value of the house: R{L} 
          Monthly interest rate: {rate}
          Number of months: {months} 
          Your monthly repayments are: R{round(loan_repayment, 2)} """)
      
else:
    print("ERROR! Please try again! ")    
    


   
        