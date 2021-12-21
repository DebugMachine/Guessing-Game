
import random 

print("welcome")
x = random.randint(1,10)

y = 5
print("Guess number between 1-10")

while y < 5: 
    value = int(input("Enter Number"))

    if value == x:
        print("You got it!")
    
        break 

    elif value < x:
        print("A little too low don't you think?",value)

    elif value > x: 
        print("A little too high dont you think?",value)

    y =y+1

    if not y < 5:
        print("5 tries over, try again")



        


