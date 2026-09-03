# 1. In one sentence: what Python keyword replaces C#'s else if?
# elif

# 2. What does this print?

x = -3
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative") # negative
    
# 3. What does this print?

items = []
if items:
    print("has items")
else:
    print("empty or falsy") #empty or falsy
    
#4. What does this print?

flag = "False"
if flag:
    print("truthy")
else:
    print("falsy") # Truthy
    
# 5. What prints, and — critically — does check_b() get called?

def check_a():
    print("A")
    return False
 
def check_b():
    print("B")
    return True
 
result = check_a() and check_b() # A, check_b never gets run since check_A amounts to false
 
# 6. Predict the value (not just True/False) assigned to y:

y = 0 or "backup" # since its an Or, the first truthy is backup

# 7. Is this valid Python, and if so what does it evaluate to when x = 5?

1 < x < 3 # yes, false

# 8. A junior dev on your team writes this to guard against a missing user ID before a database lookup:

def get_user_display_name(user_id):
    if user_id:
        return db.lookup(user_id)
    return "Guest"
 
# db.lookup(0) is a real, valid lookup in your system (user IDs are 0-indexed and user 0 exists). 
# What’s wrong with this guard, concretely — what input breaks it, and what should replace if user_id:?

# We should make sure that user_id is not < 0 and user_id != none ALSO
# if user_id: is falsy for user_id = 0, which is a real, valid ID in this system — so 
# user 0’s lookup gets silently skipped and everyone with ID 0 gets treated as a guest. 
# The bug shows up specifically for the one user ID most likely to exist (0) and nowhere else, 
# which is exactly the kind of bug that survives testing with IDs like 1, 2, 42 and 
# only surfaces in production. 
# Fix: check intent explicitly — 
# if user_id is not None: — since the real question is “was an ID provided,” not “is the ID truthy.”

#9. What prints? (This mixes truthiness ordering with short-circuit or.)

def a():
    print("eval a")
    return []
 
def b():
    print("eval b")
    return "fallback"
 
result = a() or b()
print(result) # prints "eval a" and returns []. Since its an "or" and it gives the first falsy, which is the empty set

# 10. Explain the bug, and fix it: 
# a teammate coming from C#'s bitwise-flag background writes a permission check like this, 
#  and it always seems to log both sides even when the first check already fails:

def has_read_access(user):
    print("checking read")
    return user.role in ("admin", "editor", "viewer")
 
def has_active_session(user):
    print("checking session")
    return user.session is not None and not user.session.expired
 
if has_read_access(user) & has_active_session(user):
    grant_access()
 
# What’s actually wrong here (name the specific operator misuse), and what’s the fix?

# instead of the bitwise, to make sure both conditionals are met use AND 