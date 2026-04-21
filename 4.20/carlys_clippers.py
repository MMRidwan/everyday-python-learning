hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
counter = 0
for price in prices :
  total_price += price
  counter +=1

average_price = total_price / counter

print(total_price)
print(f"Average Haircut Price: {average_price}")

new_prices = [new_price - 5 for new_price in prices]

print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)) :
  total_revenue += (prices[i] * last_week[i])

print(f"Total Revenue: {total_revenue}")

average_daily_revenue = total_revenue / 7

cuts_under_30 = []

for j in range(len(hairstyles)) :
  if prices[j] <= 30 :
    cuts_under_30.append(hairstyles[j])

print(cuts_under_30)


