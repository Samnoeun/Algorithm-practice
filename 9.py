# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# string = "3 4 5 6"
# for i in range(len(string)):
#     if string[i] != " ":
#       print(string[i],end="")
# Q2 - Multiple each letter by 2 result = "6 8 10 12"
number = "3 4 5 6"
result = 0
total = " "
for i in range(len(number)):
    if number[i] != " ":
      result = int(number[i])*2
      total += str(result) + str(" ")
print(total)
 