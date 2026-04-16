# Flatten a nested list — one level deep
# Given a list that contains integers and/or lists of integers (one level of nesting only), return a flat list of all integers in order.
# flatten([1, [2, 3], 4, [5, 6], 7]) → [1, 2, 3, 4, 5, 6, 7] flatten([1, 2, 3]) → [1, 2, 3] flatten([[1, 2], [3, 4]]) → [1, 2, 3, 4]

def flatten(listValues) :
    flattenedVal = []
    for eachValue in listValues :
        if isinstance(eachValue, list)  :
            for value in eachValue :
                flattenedVal.append(value)
        elif isinstance(eachValue, int) :
            flattenedVal.append(eachValue)

                
    return flattenedVal

print(flatten([1, [2, 3], 4, [5, 6], 7]))