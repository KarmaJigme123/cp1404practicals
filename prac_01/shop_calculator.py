
"""
CP1404: Practical 1
Student name: Karma Jigme Wangchuk
Program: Shop calculator
"""

DISCOUNT = 0.1
total_price = 0

num = int(input("Number of items: "))

while num < 0:
    num = int(input("Number of items: "))

for items in range(num):
    price = float(input("Price of item: "))
    total_price += price

discount_price =  (total_price * DISCOUNT)
final_price = total_price - discount_price
print(f"Total price for {num} items is ${final_price}")


