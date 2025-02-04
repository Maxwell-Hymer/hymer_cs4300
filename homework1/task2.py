# Test for integers
def integers_demo(a, b):
    # Example integer operation via addition
    return a + b 

# Test for floating point values
def floating_value_demo(a, b):
    # Example float operation via multiplication
    return a * b

# Test for strings
def string_demo(greeting, name):
    # Example string operation via string contactonation
    return f"{greeting}, {name}!"

# Test for booleans
def boolean_demo(boolean_one, boolean_two):
    # Example boolean operation via a "and not" conditional
    return boolean_one and not boolean_two

if __name__ == "__main__":
    print(integers_demo(4,10))
    print(floating_value_demo(3.1, .5))
    print(string_demo("Hey", "Ted"))
    print(boolean_demo(True, False))