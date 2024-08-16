# Ex3 - String
# Enter text and check if it contains capital letter or not
text = input("Enter text: ")
is_Found = False
for i in range(len(text)):
  if text[i].isupper():
    is_Found = True
if is_Found:    
    result = ("Yes")
else:
    result = ("No")    
print(result)    
