def check_a():
    print("checking a")
    return False
 
def check_b():
    print("checking b")
    return True
 
if check_a() and check_b():  # prints "checking a" only — check_b() never runs
    pass
 
if check_a() & check_b():     # prints BOTH — no short-circuit, and it's a bitwise AND on bools
    pass