myTup = ()
print(myTup)
myTup = (1,2,3)
print(myTup)
myTup = (1,"Hello",3.4)
print(myTup)
myTup = ("mouse",[8,4,6],(1,2,3))
print(myTup)
# Its indexing time!
myTup = ("p","e","r","m","i","t")
print(myTup[0])
print(myTup[5])
# We are getting nested
nTup = ("mouse",[8,4,6],(1,2,3))
# WOW a nested index
print(nTup[0][3])
print(nTup[1][1])
# Slicing and dicing
print("Sliced:",myTup[1:4])
# We iterate
for letter in (myTup):
    print("Hello",letter)
nTup[1][2] = 26
print(nTup)