out = []
for i in range(5): # for i = 0; i <5; i++
    if i == 2:
        continue  # start back at the for and i++    
    if i == 4:
        break        
    out.append(i)
print(out)  

#0 1 3