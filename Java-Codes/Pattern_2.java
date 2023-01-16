// Step 1 = Outer loop is for no of Rows
// Step 2 = a) Identify for every row how many coloums are there
//          b) identify what to do you want to print
//          c) Check after the loop is there need of new line


class Pattern2
{
    public static void main(String[] args) {
        pattern(5);
    }

    static void pattern(int n)
    {
        for (int row = 0; row<2*n ; row++) 
        {
           int totalcol = row > n ? row:n-row  ;
           
           for (int s = 0; s < row; s++) 
           {
             System.out.print(" ");
           }
           for (int colm = 0 ; colm<totalcol;colm++)
           {
            System.out.print( " *");
           } 
           System.out.println();
        }
    }
}