# Enter your monthly income
monthly_income = float(input("Enter your monthly_income: "))

# Ask for their total expenses
monthly_expenses = float(input("Enter your monthly_expenses: "))

# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses


#project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# output the resullts
print("\n----- Savings Report -----")
print(f"Your monthly saving are: {monthly_savings:.2f}")
print(f"Your projected annual savings (with 5% interest) are: {projected_savings:.2f}")
