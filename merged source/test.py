

def testFunc(param1, param2="NotInput"):
    print("called " + str(param1) + " " + str(param2))


List = [1, 2]

testFunc(*List)

print("11{0}".format("ok"))

string = "     4,3,"
print(string.replace(",", ""))
print(string.replace(""))