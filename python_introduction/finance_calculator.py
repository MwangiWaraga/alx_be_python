monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your montly savings are " + "$" + str(monthly_savings) + ".")
projected_savings =  str(int(monthly_savings * 12 + (monthly_savings * 12 * 0.05)))
print("Projected savings after one year, with interest, is: " + "$" + str(projected_savings) + ".")