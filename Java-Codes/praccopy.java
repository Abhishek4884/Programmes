 class Pattern
{
    void run(int n)
   {
     for (int row = 0; row <= n ; row++)
     {
      for(int i = 0;i<n-row;i++)
      {
        System.out.print(" ");
      }
      for (int col = 0; col <row; col++) 
      {
        System.out.println(" *");
      }
      System.out.println();
     }
   }
}


 class praccopy
{
  public static void main(String[] args) 
  {
    Pattern p = new Pattern();
    p.run(5);
  }
  
}