# # FORMAT SPECIFIERS -(NEW PYTHON STYLE)

#format() method (cannot evaluate expressions directly inside {})
name = "Kesh"
goals ="30"

print ("Welcome {}!" .format(name))
print ("{} scored {} goals" .format(name, goals))


# f-strings (Can evaluate expressions directly inside {})
name ="Daniel"
goals ="40"

print (f"Welcome {name}")
print (f"{name} scored {goals} goals")
