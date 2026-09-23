# initialize dictionary
D = {'Codingal' : 2, 'is' : 1, 'best' : 3, 'for' : 2, 'Coding' : 10}

# Initialize value
n = int(input("Enter n : "))


#Using loop
# Selective key values in dictionary
res = 0
for k in  D.keys():
    if D[k] == n:
         res = res + 1

# printing results
print("Frequency of",n ,"is : " + res)