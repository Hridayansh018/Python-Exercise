n = [1,2,3,4,5,6,7,8,9,10,11]

for i in range (1,11):
    if i % 2 == 0:
        continue
    print(int(i**2))


########################################################################################################################

expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input("Enter an expense amount: "))

if min(expense_list) <= expense <= max(expense_list):
    month_index = expense_list.index(min(expense_list, key=lambda x: abs(x - expense)))
    print(f"The expense of {expense} occurred in month {month_index + 1}.")
else:
    print("Expense not found in the range of given data.")
