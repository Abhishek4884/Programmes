def Display(No):
  
    if(No<=1):
        return 1
    else:
        return(No * Display(No-1))



def main():
    print("Enter the number :")
    Num = int(input())

    print(Display(Num))

if __name__=="__main__":
    main()