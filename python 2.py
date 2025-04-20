basic_salary = 40000.0
bonus = 5000.0
allowances = 3000.0

gross_salary = basic_salary + bonus + allowances

pf = basic_salary * 0.12
income_tax = gross_salary * 0.10
net_salary = gross_salary - pf - income_tax

print("Basic Salary:", basic_salary)
print("Bonus:", bonus)
print("Allowances:", allowances)
print("Gross Salary:", gross_salary)
print("Provident Fund (12% of Basic Salary):", pf)
print("Income Tax (10% of Gross Salary):", income_tax)
print("Net Salary:", net_salary)
