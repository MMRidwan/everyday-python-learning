# Python Conditionals – Cheat Sheet

## Overview

Conditional statements control the flow of execution in a program. Instead of running code sequentially, Python allows decision-making using conditions.

A condition evaluates to either `True` or `False`, and based on that result, different blocks of code execute.

---

## Core Syntax

### Basic `if`

```python
if condition:
    # code runs if condition is True
```

---

### `if / else`

```python
if condition:
    # runs if True
else:
    # runs if False
```

---

### `if / elif / else`

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition2 is True
else:
    # runs if none are True
```

* Only **one block executes** in the chain

---

## Indentation (Critical Rule)

Python uses indentation to define blocks of code.

```python
if True:
    print("Inside block")

print("Outside block")
```

* Incorrect indentation breaks logic or causes errors

---

## Boolean Expressions

Conditions are built using comparisons:

```python
x > y
x == y
x != y
x <= y
```

These evaluate to `True` or `False`.

---

## Logical Operators

### `and`

Both conditions must be true:

```python
if a > 0 and b > 0:
```

### `or`

At least one must be true:

```python
if a > 0 or b > 0:
```

### `not`

Reverses condition:

```python
if not is_valid:
```

---

## Short-Circuit Behavior

Python stops evaluating once the result is determined.

Example:

```python
if True or (1/0):
    print("No error")
```

The second part is never evaluated.

---

## Conditional Expression (Ternary)

```python
result = "A" if condition else "B"
```

* Compact alternative to `if/else`
* Should be used only for simple logic

---

## One-Line `if` (Not Recommended for Complex Logic)

```python
if condition: print("Hello")
```

* Works, but reduces readability

---

## Nested Conditionals

```python
if condition:
    if another_condition:
        # nested logic
```

* Avoid deep nesting — makes code hard to read

---

## `pass` Statement

Used as a placeholder:

```python
if condition:
    pass
```

---

## Best Practices

* Keep conditions simple and readable
* Avoid deeply nested `if` statements
* Use meaningful variable names
* Prefer clarity over cleverness

---

## Mental Model

* `if` → decision
* `elif` → alternative decision
* `else` → fallback
* indentation → structure

---

## Common Mistakes

* Wrong indentation
* Using `=` instead of `==`
* Overusing nested conditions
* Writing unreadable one-liners

---

## Summary

* Conditionals control program flow
* Python uses indentation for structure
* Only one branch executes in an `if/elif/else`
* Logical operators allow combining conditions
* Simplicity and readability are critical
