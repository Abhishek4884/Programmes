
Data = [11,12,13,14,15]

print("Output using for")
for no in Data:
    print(no,end = " ")
print()

print("Output using for with index")
for i in range(0,len(Data)):
    print(Data[i] , end = " ")
print()

print("Output using while with index")

i = 0
while(i<len(Data)):
    print(Data[i] , end = " ")
    i=i+1

