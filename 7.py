# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
out_range = False
while not out_range:
    number = int(input("Enter number: "))
    if number > 10 and number < 20:
        print("Continue")
    else:
        print("Out of range")    
        out_range = True    