ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for counter in ages :
    if counter == 34 :
        continue
    # print(counter)
    

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13], 5, "string"]

for data in sales_data :
    if isinstance(data, list) :
        for data_one in data :
            print(data_one)