# Sales Data Aggregator
# Given a 2D list sales_data where each inner list represents the sales figures for a region, write a program that:

# Identifies and labels each inner list by its array number
# Calculates and prints the total sales for each individual region
# Calculates and prints the grand total across all regions

# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# Array Number 1 : [12, 17, 22]
# Array Total: 51
# Array Number 2 : [2, 10, 3]
# Array Total: 15
# Array Number 3 : [5, 12, 13]
# Array Total: 30
# Grand Total: 96

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]


total_total = 0
array_count = 0

# Loop over each element of array
for each_array in sales_data :
  # check if each_element is another array
  if isinstance(each_array, list) :
      
    # if array, increment the count and set the array number
    array_count += 1
    print(f"Array Number {array_count} : {each_array}")
    
    # IMPORTANT :   each_inside_array_total outside of the internal_loop allows to print the total of each array and  reset for the next array. 
    #               This avoids a running sum of all the arrays altogether returning a total sum. Instead gives a clean each sum. 
    each_inside_array_total = 0
    for each_inside_array in each_array :
        each_inside_array_total += each_inside_array
    print(each_inside_array_total)
    
    total_total += each_inside_array_total

print(total_total)


  