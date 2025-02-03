# Test for integers
def integers_demo():
    a = 5
    b = 3
    # Example integer operation
    return a + b 

# Test for floating point values
def floating_value_demo():
    a = 2.5
    b = -1.15
    # Example float operation
    return a * b

# Test for strings
def string_demo():
    greeting = "Hello"
    name = "Max"
    # Example string operation
    return f"{greeting}, {name}!"

# Test for booleans
def boolean_demo():
    is_true = True
    is_false = False
    # Example boolean operation
    return is_true and not is_false

if __name__ == "__main__":
    print(integers_demo())
    print(floating_value_demo())
    print(string_demo())
    print(boolean_demo())