#Python Day 1 assignment
#Take inputs from user and convert them into list  and also arrange the list in descending order

x = input('Enter the values :  ').split()
print(x)
y = [int(i) for i in x]
y.sort()
y.reverse()
print (y)