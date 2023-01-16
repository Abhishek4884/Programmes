print("Demonstration of Tuple")

# Data : Heterogeneous
# Ordered : No
# Indexed : No
# Mutable : Yes
# Duplicates : No
data = {11,21,51,101,21,11}
data1 = {11,90.25,True,"Hello"}
print("Data is Hetrogeneous : " , data1)
print("Data is ordered :" ,data1)
#print("Data at Index : " ,data1[2])
print("Data with Duplicates : " ,data )
print("Set is mutable")
data.add(101)

print(data)
print("List is mutable")
data.discard(1223)
print(data)
