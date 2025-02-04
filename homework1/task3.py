def if_statement_demo(a):
    value_state = None

    if a > 0:
        value_state = "Positive"
    elif a < 0:
        value_state = "Negative"
    else:
        value_state = "Zero"

    return value_state

    

def for_loop_demo():
    prime_numbers = []
    num = 2  # Start checking for primes from 2

    # For loop to find the first 10 prime numbers
    for _ in range(10): 
        # Keep checking until we find a prime 
        while True:  
            is_prime = True
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break

            # Exit the while loop once we find a prime
            if is_prime:
                prime_numbers.append(num)
                break 
            # Check the next number 
            num += 1  

        # Move to the next number to check for the next prime
        num += 1  

    return prime_numbers

def while_loop_demo():
    sum_to_hundred = 0
    counter = 1

    while counter <= 100:
        sum_to_hundred += counter
        counter += 1

    return sum_to_hundred

if __name__ == "__main__":
    print(if_statement_demo(0))
    print(for_loop_demo())
    print(while_loop_demo())