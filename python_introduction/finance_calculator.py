# prompt the user for their monthly income
monthly_income = int(input("Enter  your monthly_income: "))

# Ask for their total expenses
monthly_expense = int(input("Enter your monthly_expenses: "))

# calculate monthly savings
monthly_savings = monthly_income - monthly_expense

print(monthly_savings)

#project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# output the resullts
print("Your monthly saving is:", monthly_savings)
print("Your projected annual savings after 5% interest is:", projected_savings)
