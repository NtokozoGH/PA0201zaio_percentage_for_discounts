1.1
def calculate_discount(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return discount_amount, final_price

original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount_amount, final_price = calculate_discount(original_price, discount_percentage)

print(f"Discount amount: {discount_amount:.2f}")
print(f"Final price after discount: {final_price:.2f}")

#question 2
mark = float(input("Enter your mark: "))
if mark >= 75:
    grade = "Distinction"
elif mark >= 60:
    grade = "Merit"
elif mark >= 50:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Result: {mark}% - {grade}")

#question 3
current_salary = float(input("Enter your current salary: "))
increase_percentage = float(input("Enter the percentage increase: "))

increase_amount = (increase_percentage / 100) * current_salary
new_salary = current_salary + increase_amount

print(f"Increase Amount: {increase_amount:.2f}")
print(f"New Salary: {new_salary:.2f}")

#question 3
current_salary = float(input("Enter your current salary: "))
increase_percentage = float(input("Enter the percentage increase: "))

increase_amount = (increase_percentage / 100) * current_salary
new_salary = current_salary + increase_amount

print(f"Increase Amount: {increase_amount:.2f}")
print(f"New Salary: {new_salary:.2f}")

#question 4
cost_price = float(input("Enter the cost price of the item: "))
selling_price = float(input("Enter the selling price of the item: "))

# 2. Determine check if Profit/loss or break evev
if selling_price > cost_price:
    # Calculate Profit
    profit = selling_price - cost_price
    # Calculate Profit Percentage: (Profit / Cost Price) * 100
    profit_percentage = (profit / cost_price) * 100
    print(f"Result: Profit")
    print(f"Profit Amount: R{profit:.2f}")
    print(f"Profit Percentage: {profit_percentage:.2f}%")

elif cost_price > selling_price:
    # Calculate Loss formula 
    loss = cost_price - selling_price
    # Calculate Loss in percentage: (Loss / Cost Price) * 100
    loss_percentage = (loss / cost_price) * 100
    print(f"Result: Loss")
    print(f"Loss Amount: R{loss:.2f}")
    print(f"Loss Percentage: {loss_percentage:.2f}%")

else:
    print("Result: No Profit, No Loss (Break-even)")