def Fact(no):
    Ans = 1
    while(no >= 1):
        Ans = Ans * no
        no = no - 1
    return Ans

ret = Fact(10)
print(ret)