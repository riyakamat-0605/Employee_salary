import sys


if len(sys.argv) == 2:
    script_name = sys.argv[0]
    salary = float(sys.argv[1])
    print("User provided input salary:")
else:
    script_name = sys.argv[0]
    salary = 30000  
    print("No input given — using default salary:")


bonus = salary * 0.10
total_salary = salary + bonus


print("Script Name:", script_name)
print("Salary:", salary)
print("Bonus (10%):", bonus)
print("Total Salary:", total_salary)
