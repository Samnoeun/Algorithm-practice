# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
text = "454639"
odd_number=0
even_number=0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
print("Even number: ", even_number)
print("Odd number: ", odd_number)


# Q2 - Sum all number 
text = "454639"
sum = 0
for i in range(len(text)):
        sum += int(text[i])
print(sum)


# Q3 - Sum only even number
text = "454639"
sum = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        sum += int(text[i])
print(sum) 


# Q4 - Reverse
text = "454639"
result = ""
for i in range(len(text)):
    reverse = len(text)-1
    result += text[reverse-i]
print(result)