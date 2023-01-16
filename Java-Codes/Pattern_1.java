// Step 1 = Outer loop is for no of Rows
// Step 2 = a) Identify for every row how many coloums are there
//          b) identify what to do you want to print
//          c) Check after the loop is there need of new line


class Pattern1
{
    public static void main(String[] args) {
        pattern(4);
    }

    static void pattern(int n)
    {
        for (int row = 0; row<2*n ; row++) 
        {
            int totalcol = row > n ? 2*n-row : row;
            for(int col =0 ;col < totalcol ;col++)
            {
                System.out.print("*" + " " + "-" +" " );
            } 
                 System.out.println();
        }
    }
}