L=[["Core Programming","C","C++","DS"], ["Java Expert","Core Java","Adv.Java"], ["Python Handy","ML","Data S"]]
print(len(L))
print(L[1])
#1 Printing Without Loop
print(L)

#2 Printing With Loop
print()
for i in range(0, len(L)):
    for j in range(0,len(L[i])):
        print(L[i][j])
