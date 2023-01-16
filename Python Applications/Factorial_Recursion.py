def Fact(no):

    if(no <= 1):
        return 1
    else:
        return (no * Fact(no-1))

ret = Fact(5)
print(ret)