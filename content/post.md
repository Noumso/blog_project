# Mutable, Immutable... everything is object!

![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

---

## Introduction

In Python, everything is treated as an object. Whether we deal with numbers, lists, strings, or even functions, each entity carries an identity, a type, and a value. Understanding this foundation allows developers to better predict how Python handles memory, variables, and data manipulation behind the scenes.

---

## ID and Type

Each Python object has a unique **ID** (memory address) and a **type** that defines its nature. We can access them using the built-in `id()` and `type()` functions.

```python
x = 10
print(id(x))  # e.g., 140432312634800
print(type(x))  # <class 'int'>
```

Assigning variables doesn't create a new object unless the value changes, reinforcing that variables are simply references to objects.

---
## Mutable Objects

Mutable objects can be altered after creation. Lists, dictionaries, and sets are common mutable types.

```python
my_list = [1, 2, 3]
print(id(my_list))
my_list.append(4)
print(id(my_list))  # Same ID, different content
print(my_list)
```

Mutating an object does not affect its ID, only its internal state.

---

## Immutable Objects

Immutable objects cannot change once created. Typical examples include integers, floats, strings, and tuples.

```python
name = "python"
try:
    name[0] = "P"
except TypeError:
    print("Cannot modify an immutable object!")
```

When we attempt to "change" an immutable object, Python actually creates a new object:

```python
a = 5
print(id(a))
a += 1
print(id(a))  # Different ID!
```

---
## Why Does It Matter?

Understanding mutability is crucial because it affects how Python manages memory and variables. For example, using mutable default arguments in functions can lead to unexpected behaviors:

```python
def add_element(item, target=[]):
    target.append(item)
    return target

print(add_element(1))  # [1]
print(add_element(2))  # [1, 2] — NOT a fresh list!
```

This happens because the same list object is reused across function calls. Being aware of mutability helps avoid such hidden bugs.

---

## How Arguments Are Passed to Functions

Python passes object references to functions, not copies.
The behavior depends on whether the object is mutable or immutable.

Mutable case:

```python
def modify_list(lst):
    lst.append(100)

nums = [1, 2, 3]
modify_list(nums)
print(nums)  # [1, 2, 3, 100]
```

Immutable case:

```python
def modify_number(n):
    n += 1

x = 10
modify_number(x)
print(x)  # Still 10
```

For immutable objects, any "change" inside the function does not affect the original variable.

---

## Conclusion

Understanding the distinction between mutable and immutable objects is vital for mastering Python's internals. It influences how variables behave, how memory is managed, and how to write safer and more efficient code.
Always remember: everything in Python is an object, and knowing how to interact with those objects unlocks the real power of the language!