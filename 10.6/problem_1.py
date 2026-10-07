# Problem 1 — Safe Config Value Parsing (difficulty: Easy · not a direct LeetCode problem - classic phone-screen/take-home pattern, safe-parse/config-defaulting utility)

# This exact shape is the first thing you write in any config loader, query-param handler, or env-var reader: the raw value might be a clean number, might be garbage text, or might be entirely missing (None) because the key wasn’t set at all. Getting the “missing” case right alongside the “garbage” case is what separates a working loader from one that crashes the first time a field is optional.

# Problem: Write parse_int_or_default(raw, default=0) that converts raw to an int, returning default for anything that can’t convert — including raw being None.

# parse_int_or_default("42") → 42
# parse_int_or_default("abc") → 0
# parse_int_or_default("3.5", default=-1) → -1
# parse_int_or_default(None) → 0


def parse_int_or_default(raw, default=0):
    if(raw is None):
        return default
    
    try:
        return int(raw)
    except (ValueError, TypeError, KeyError):
        return default
    
print(parse_int_or_default("42") )
print(parse_int_or_default("abc"))
print(parse_int_or_default("3.5", default=-1))
print(parse_int_or_default(None))

