# Problem 4
# hard
# Count words in a sentence
# Given a sentence string, return a dictionary where each key is a unique word (case-insensitive) and its value is how many times it appears. 
# Punctuation should be stripped. Do not use any library like collections.
# count_words("the cat sat on the mat the cat") → {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1} count_words("Hello hello HELLO") → {"hello": 3}

# def create_list(string) :
#     stringList = []
    
#     stringSplit = ""
    
#     for char in range(len(string)) :
#         if string[char] == " ":
#             stringList.append(stringSplit.lower())
#             stringSplit = ""
#         elif string[char] in ",!?|/":
#             continue
#         else :
#             stringSplit = stringSplit + string[char]
   
#     stringList.append(stringSplit.lower())
    
#     return stringList

# def count_words(string) :

#     stringList = create_list(string)

#     newDict = {}

#     for eachValue in stringList :
#         if eachValue in newDict :
#             newDict[eachValue] = newDict[eachValue] + 1
#         else :
#             newDict[eachValue] = 1

def create_list(string) :
    stringList = []
    
    for char in string.lower().split() :
        char = char.strip(".,!?;")
        stringList.append(char)
    
    return stringList
    
    
def count_words(string) :

    stringList = create_list(string)

    newDict = {}

    for eachValue in stringList :
        newDict[eachValue] = newDict.get(eachValue, 0) + 1

    return newDict

print(count_words("I am Human I am Human"))
print(count_words("the cat sat on the mat the cat"))
print(count_words("Hello hello HELLO"))