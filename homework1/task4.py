def calculate_discount(price, discount):
    # Calculate the final price after applying a discount
    return price - (price * (discount / 100))

if __name__ == "__main__":
    print(calculate_discount(2500, 50))