#Jefferson Ganac
# IT-103

salary = float(input("Enter your monthly salary: "))
loan = float(input("Enter your loan amount: "))

if(salary>=30000):
    max_loan = salary * 10
    if(loan <= max_loan):
        print("You are eligible for a loan")
        months = int(input("Enter months to pay: "))
        interest = loan * 1.10
        monthly = interest / months
        print(f"Your total loan amount with 10 interest is {interest:.1f}")
        print(f"Your monthly payment over {months} months is {monthly:.1f}")
    else:
        print("You are not eligible for a loan: High Loan Amount")
else:
    print("You are not eligible for a loan: Low Salary")