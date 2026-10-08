for i in range(3):
    for j in range(3):
        if j == 1:
            print(f"breaking inner at i={i}, j={j}")
            break
    print(f"outer i={i} continues") # this only runs after breaking
    
    
# i at 0 -> j at 0
# outher i = 0 continues

# i at 0 -> j at 1
# breaking inner at i=0, j = 1
# outer i = 0 continue

# i = 1 -> j at 0
# outer i = 1 Continues

# i = 1 -> j = 1
# breaking innner at i = 1, j = 1
# outer i = 1 continues

# i = 2 -> j at 0
# outer i = 2 Continues

# i = 2 -> j = 1
# breaking innner at i = 2, j = 1
# outer i = 2 continues