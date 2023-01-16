def main():
    print("Enter the num")
    num = int(input())
    maxx = 0
    
    while(num>0):
        rem = num %10
        
        if(rem >maxx):
            maxx = rem
        num = num /10
    print(maxx)

if __name__ == "__main__":
    main()