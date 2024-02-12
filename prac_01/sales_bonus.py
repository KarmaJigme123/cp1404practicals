"""
CP1404 - Practical 1
Student name: Karma Jigme Wangchuk

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MAX_BONUS_BOUNDARY  = 1000
TEN_PERCENT_BONUS = 0.1
FIFTEEN_PERCENT_BONUS = 0.15

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < MAX_BONUS_BOUNDARY:
        bonus = sales * TEN_PERCENT_BONUS
    else:
        bonus = sales * FIFTEEN_PERCENT_BONUS

    print(f"Bonus = {bonus}$")
    sales = float(input("Enter sales: $"))
