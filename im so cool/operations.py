myDict = {}
myDict = {1:"apple",2:"ball"}
myDict = {"name":"John",1:[2,4,3]}
myDict = {"name":"Jack","age":26}
print(myDict["name"])
print(myDict.get("age"))
myDict["age"] = 27
print(myDict)
myDict["address"] = "Downtown"
print(myDict)
myDict.pop("age")
print(myDict)
print("Address: ",myDict.get("address"))
myDict.clear()
print(myDict)