# Question

# Given an hour (0–23):

# 5–11 → "Morning"
# 12–17 → "Afternoon"
# 18–21 → "Evening"
# Otherwise → "Night"

hour = int(input("What hour to check : "))
time = ""

# match hour :
#     case hour >= 5 and hour <= 11 :
#         time = "Morning"

if 5 <= hour <= 11 :
    time = "Morning"
elif 12 <= hour <= 17 :
    time = "Afternoon"
elif 18 <= hour <= 21 :
    time = "Evening"
else :
    time ="Night"

print(time)
    
    
# Expert
# def get_period(hour):
#     if 5 <= hour <= 11:
#         return "Morning"
#     if 12 <= hour <= 17:
#         return "Afternoon"
#     if 18 <= hour <= 21:
#         return "Evening"
#     return "Night"

# print(get_period(hour))