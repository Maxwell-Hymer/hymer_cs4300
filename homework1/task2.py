def main():
    # Test for integers
    def integers_demo():
        int a = 5
        int b = 3
        # Example integer operation
        return a + b 

    # Test for floating point values
    def floating_value_demo():
        float a = 2.5
        float b = -1.15
        # Example float operation
        return a * b

    # Test for strings
    def string_demo():
        str greeting = "Hello"
        str name = "Max"
        # Example string operation
        return f"{greeting}, {name}!"

    # Test for booleans
    def boolean_demo():
        bool is_true = True
        bool is_false = False
        # Example boolean operation
        return is_ture and not is_false

if __name__ == "__main__":
    print(integers_demo())
    print(floating_value_demo())
    print(string_demo())
    print(boolean_demo())