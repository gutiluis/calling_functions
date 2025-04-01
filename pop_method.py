# pop method returns last element always
#print(["a", "b", "c"].pop())

# list constructor
#print(list(["a", "b", "c"]).pop())
#print(list(("make a list")).pop())
#a = list("make a list").pop()
#print(a)



# list comprehension
c = [x for x in [1, 2, 3, 4]].pop()
#print(c)

a = [x for x in range(2)].pop()
#print(a)

weapons = ["gun", "bomb", "granade"]
#print([x for x in a].pop())
#print([x for x in a if x == "gun"].pop())
#print([x for x in a if x == "bomb"].pop())
#print([x for x in a if x is not True].pop())
#print([i for i in a if i is "gun"].pop())
#print([i for i in a if i != "bomb"].pop())
print([i for i in weapons if "bomb" in weapons].pop())

#a = "something"
#print(sorted(a).pop())
#print(sorted(a, reverse=True).pop())

