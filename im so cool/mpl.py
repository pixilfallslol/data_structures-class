import matplotlib.pyplot as plt
import pandas as pd

studentNames = ["Marcus","Alexander","Prince"]
studentMarks = [36,23,55]

marksPerc = []

for x in range(len(studentMarks)):
    res = (x/50)*100
    marksPerc.append(res)

print(marksPerc)

def mlc(m1, m2):
    plt.plot(m1,m2)
    plt.title("Marks YAY")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.show()
    
mlc(studentNames,studentMarks)

def pbc(s, m):
    plt.bar(s,m)
    plt.title("BAR BAR BAR BAR BAR BAR BAR BAR BAR")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()
    
pbc(studentNames,marksPerc)