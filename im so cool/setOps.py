sec = {1,2,2,3,4,4,4}
print("Set: ",sec)
sec1 = sec
sec2 = {2,4,4,6}
print("\nSet 1 "+str(sec1))
print("Set 2 "+str(sec2))
print("Diff")
print(sec1.difference(sec2))
print("SD")
print(sec1.symmetric_difference(sec2))
sec.add(5)
print("Updated Set: "+str(sec))