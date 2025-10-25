#Mirach Erkol
#10/25/2025
#1.3 Assignment
#CSD325-340A Advanced Python

#Git Link https://github.com/Mikey5007/csd-325/tree/main/module-1

#Ask the user how many bottles of beer are on the wall.
#Pass that input to a function that manages the countdown.
#The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
#Once the count is down to 1, change lyrics to show "1 bottle of beer..."
#At the end of the countdown, get back to the main program and remind the user to buy more beer.


def countdown(bottles):
    # Keep looping as long as there is at least 1 bottle left
    while bottles > 0:
        # If there is more than one bottle, use plural
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
        else:
            # When only one bottle remains, switch to singular wording
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")

        # Subtract one bottle for the next verse
        bottles -= 1

    # When the loop ends (no bottles left), print a message
    print("Time to buy more bottles of beer.")

#main function
def main():
    # Ask the user to enter a number of bottles
    try:
        num_bottles = int(input("Enter number of bottles: "))
        # Call the countdown function using the user's number
        countdown(num_bottles)
    except ValueError:
        # If the user types something that isn’t a number, show an error
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
