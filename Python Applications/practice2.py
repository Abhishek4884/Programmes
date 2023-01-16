def main():
    Arr = list()

    print("Enter The values you Want to Store : ")
    Size = int(input())

    print("Enter The values :")

    for i in range(0,Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

if __name__== "__main__":
    main()
