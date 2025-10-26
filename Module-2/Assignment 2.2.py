# Mirach Erkol
# 10/10/2025
# CSD205-340A
# Assignment 2.2 (Redo)

# Program for calculating the cost of fiber optic cable.

def get_length_needed():
    # Get the number of feet of fiber optic cable needed with basic validation
    while True:
        try:
            return int(input("Please input how many feet of fiber optic cable you will need: "))
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 150).")

def calculate_cost(length_needed):
    # Calculate cost based on the correct tier boundaries
    if length_needed <= 100:
        price_per_foot = 0.87
    elif length_needed <= 250:
        price_per_foot = 0.80
    elif length_needed <= 500:
        price_per_foot = 0.70
    else:
        price_per_foot = 0.50
    cost = length_needed * price_per_foot
    return price_per_foot, cost

def display_results(length_needed, price_per_foot, cost):
    # Display results
    print(f"The total cost for {length_needed} feet of fiber optic cable is ${cost:.2f}.")
    print(f"You received a bulk order discount — your cost is ${price_per_foot:.2f} per foot!")
    print("Thank you for shopping with Fiber Optics R Us.")

def main():
    # Display welcome message
    print("Hello, welcome to Fiber Optics R Us!")
    length_needed = get_length_needed()
    price_per_foot, cost = calculate_cost(length_needed)
    display_results(length_needed, price_per_foot, cost)

if __name__ == "__main__":
    main()
