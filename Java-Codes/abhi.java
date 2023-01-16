class First
{
  void display ()
  {
   System.out.println("This is display");

  }
}

class Second
{
  First meth()
  {
    First f=new first();
    return f;
  }
}

class Demo
{
  public static void main(String args[])
  {
    Second s = new Second();
    First f1;
         f1=s.meth();
         f1.display();

   }
}