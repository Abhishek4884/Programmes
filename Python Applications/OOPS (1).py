class BookStore:
    NoOfBooks = 0
    def __init__(self , Name , Author):
        self.Name = Name
        self.Author = Author

    def Display(self):
        print( self.Name, self.Author ,"NO of Books :", BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming by" , "Robert Love." )
    BookStore.NoOfBooks= 1
    obj1.Display()

    obj2 = BookStore("C Programming by" , "Dennis Ritche.")
    BookStore.NoOfBooks= 2
    obj2.Display()

if __name__=="__main__":
    main()