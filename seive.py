def sieve_of_eratosthenes_generator(limit=1000):
    """
    Generates prime numbers up to a specified limit 
    using the Sieve of Eratosthenes.
    """
    # Initialize a boolean list tracking primality
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    for number in range(2, limit + 1):
        if is_prime[number]:
            # Yield the prime number and pause execution
            yield number
            
            # Mark multiples of the found prime as non-prime
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

def main():
    # Initialize the generator
    prime_gen = sieve_of_eratosthenes_generator()
    
    print("Press 'Enter' to get the next prime number. Type 'q' and press Enter to quit.\n")
    
    count = 0
    while count < 52:
        user_input = input(f"Press Enter for prime #{count + 1}: ")
        
        # Allow the user to exit early
        if user_input.strip().lower() == 'q':
            print("Exiting.")
            break
            
        try:
            # Fetch the next prime from the generator
            next_prime = next(prime_gen)
            count += 1
            print(f"-> {next_prime}")
        except StopIteration:
            print("Reached the limit of the sieve.")
            break
            
    if count == 52:
        print(f"\nSuccess! You reached the 52nd prime number.")

if __name__ == "__main__":
    main()