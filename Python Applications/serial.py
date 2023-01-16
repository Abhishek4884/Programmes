def Square(No):
    return (No*No)

def main():
    Data = [1996566,29859626,38965466,5959664,5985965]

    Result = []
    for value in Data:
        Result.append(Square(value))

    print("result sfter Square " , Result )

if __name__=="__main__":
    main()