#Elliott Morris, 2/4/2026, Dice
import random

def randDice():
    #roll two dice (1-6) and return their sum
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1 + die2

def get_suffix(n):
    #gets the suffix (1st, 2nd, 3rd) for good displaying
    #Handles 11, 12, and 13
    if 10 <= n % 100 <= 20: #finds if a number is between 10 and 20
        return "th"
    #handles other endings
    else:
        return {1:"st", 2:"nd", 3:"rd"}.get(n%10, "th") #assigns the correct suffix

def main():
    total = 0
    for count in range(1,101):
        dice_result = randDice()
        suffix = get_suffix(count)
        total += dice_result
        print(f"The {count}{suffix} dice result is: {dice_result}")

    average = total / 100
    print(f"The total of all rolls was {total}.")
    print(f"The average of all rolls was {average:.2f}")

if __name__ == "__main__":
    main()
