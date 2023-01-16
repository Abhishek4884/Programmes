

Batches = {"ppa" : 18000 , "Python" : 16500 , "LB" : 16500 , "Angular" : 15000}

print("Data of Dictionry :" , Batches)

print("Data traversal using for loop")
for x in Batches:
    print(x )

print("Data traversal using for loop")
for x in Batches:
    print(x ,Batches[x])


print("Data traversal using for loop")
for x in Batches:
    print(x ,Batches.get(x))

keyBatches = Batches.keys()
print(type(keyBatches))
print(keyBatches)

valueBatches = Batches.values()
print(valueBatches)

for i in range(0,len(Batches)):
    print("Batch name is :" , keyBatches[i] , end = " ")
    print("Fees are :" , valueBatches)














