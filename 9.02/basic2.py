#Why this matters concretely: 
# the pattern if some_list: is genuinely idiomatic Python for “is this list non-empty” 
# — that’s not lazy code, it’s how experienced Python developers write it, equivalent to your if (list.Any()). 
# The trap is when you use the same shorthand meaning to check for “is this None” and it silently also catches empty-but-valid values:

def process(items):
    if items is not None:
        return len(items)
    return "no items given"
 
print(process([])   )    # returns "no items given" — but [] is NOT None, it's a valid empty list!
print(process(None) )    # also returns "no items given"