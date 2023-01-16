def Add(A ,B):
    return A+B

def Sub(A ,B):
    return A-B

def Calculater(Target , Value1 , Value2):
    return Target(Value1 , Value2)

Ret = Calculater(Target = Add , Value1=10 , Value2=21)
    
