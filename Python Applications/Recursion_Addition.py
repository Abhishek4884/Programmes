def Display(No):
    if(No <= 0):
        return 0
    else:
        return (No + Display(No - 1))
def main():

    Ret = Display(4)
    print(Ret)

if __name__=="__main__":
    main()