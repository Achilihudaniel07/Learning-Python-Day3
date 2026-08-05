# # FORMATTING WITH INPUT()
name = input ("Enter your name:")
age = int(input ("Enter your age:"))

print ("Name: %s \n Age: %d" % (name,age))


item = input("Enter the item needed:")
price = float(input("Enter the price:"))

print ("%s costs \u20a6%.3f" % (item, price))
print ("%s costs \u20a6%.3f  %d" % (item, price, price))


# CONVERTING FLOAT INTO INTEGER
user_num = int(float("5.5"))  # Output: 5
print(user_num)