import os

def main():
    print("PID of current process :" , os.getpid())
    print("PID of parent current process :" , os.getppid())


if __name__=="__main__":
    main()