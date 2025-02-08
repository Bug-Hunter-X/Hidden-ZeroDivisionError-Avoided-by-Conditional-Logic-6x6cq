def improved_function(a, b):
    if a == 0:
        return float('inf') # Or handle it appropriately, like raising an exception or returning a default value.
    return b / a

result = improved_function(0, 10)
print(result) # Output: inf

result = improved_function(10, 0)
print(result) # Output: 0.0

result = improved_function(0,0)
print(result) # Output: inf