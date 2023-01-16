def Display(No):
    if(No > 0):
        No = No - 1
        Display(No)
        print( No)

def main():
    Display(4)

if __name__=="__main__":
    main()