
names = ["darcy", "tselmeg", "eliz", "juju"]
print(names [0] )
print(names [1] )

names.append("jul")

print(names)
 

second_names = ["huslen"] + names 
print(second_names)


for string in names:
    print(string + "   Hello?")
    print(string[0] + "   the first letter of the name")
    for c in string:
        print(c)
print("Finished")

for k in [0, 1, 2, 3, 4]:
    print(k, names[k])

hundnames = [f"name_{i}" for i in range(100)]
print(hundnames)

#hundnames = [f"name_{i}" for i in range (100)]
#print(hundnames)

print("---")
for k in range(4):
    print(k, names[k])
    print("---")
    for k in range(len(names)):
        print(k, names[k])