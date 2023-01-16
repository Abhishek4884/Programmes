print("Demonstration of Sequnce data type")

# Data : Heterogeneous
# Ordered : Yes
# Indexed : Yes
# Mutable : Yes
# Duplicates : Yes
data = [11,21,51,101,21,11]
data1 = [11,90.25,True,"Hello"]
print("Data is Hetrogeneous : " , data1)
print("Data is ordered :" ,data1)
print("Data at Index : " ,data1[2])
print("Data with Duplicates : " ,data )
print("List is mutable")
data.append(101)
print("List is mutable")
data.pop(11)
print(data)