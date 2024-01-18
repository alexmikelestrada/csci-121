apples_purchased = int(input("How many apples would you like?"))
apple_price = 4.50
total_price = apple_price * apples_purchased
tax = 2
apples_final_cost = total_price * (1+tax/100)
print("your total is $", apples_final_cost)
# using input to allow user input to influence strings
# using int to declare that the user input must be an integer
x = 12
y = 5
z = 21
print(f' it has been 3 years since I was {x + y} years old, there are {len(x)} characters')
