

def Display(No):
    Cnt = 0
    if(Cnt < No):
        print("Hello")
        Cnt = Cnt + 1
        Display(No)

def main():
    Display(4)

if __name__=="__main__":
    main()

