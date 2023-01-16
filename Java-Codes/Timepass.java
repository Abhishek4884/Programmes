class Demo
{
  public static void main(String[] args) {
    try 
    {
        int a,b,c ;
        a = 10;
        b = 0;
        c = a/b;
        System.out.println(c);
    } 
    
    catch(ArithmeticException e)
    {
        e.printStackTrace();
    }
    finally
    {
        System.out.println("Helllo");
    }
    System.out.println("Abhi");
    
  }
}