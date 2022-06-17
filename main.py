mealPrice = 0
total = 0
#inputted meal items 
meal = input("Enter the meal you would like(hashbrowns, tater tots or fried rice):")
#if/else statement determining the price for meal items
if meal  == "hashbrowns":
  mealPrice = 2.24
elif meal == "tater tots":
  mealPrice = 9.69
else:
  mealPrice = 11.59
#prints price of selected meal item
print("Price of Your Meal: $", round(mealPrice,2))

#calculates tip amount
tip = 0.23 * mealPrice
print("Tip amount:", round(tip,2)) 

#calculates total price without tax
total = mealPrice + tip
print("Total without Tax:", round(total,2))

#calculates tax
tax = total * 0.13
print("Tax:", round(tax,2))

#calculates total price with tax
totalTax = float(total + tax)
print("Total with Tax:", round(totalTax,2))
