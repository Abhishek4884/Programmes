// Step 1 = Outer loop is for no of Rows
// Step 2 = a) Identify for every row how many coloums are there
//          b) identify what to do you want to print
//          c) Check after the loop is there need of new line


class Pattern3
{
    public static void main(String[] args) {
        pattern(5);
    }

    static void pattern(int n)
    {
        for (int row = 0; row<n ; row++) 
        {
            int space = row;
            for (int i = 0; i <space; i++) {
                System.out.print(" ");
            }
           for (int col = 0; col <n-row; col++) 
           {
            System.out.print("* ");
           }
           System.out.println();
        }
    }
}