class Circle 
{  
  double radius ;

  Circle(double radius)
  {
   this.radius=radius;
    
  }
   void area()
  {
   System.out.println("Area of Circle" + "  " + 3.14*2*radius);

  }
   void circumferance()
  {
   System.out.println("Circumferance of Circle" + "  " + 3.14*radius*radius);

  }
}

class First

{
  Circle meth()
  {
   Circle f = new Circle(10);
   return f;
  }
}

class Return
{
  public static void main(String args[])

  {
    First f1 = new First();
    Circle c1 ;
      c1= f1.meth();
      c1.area();
      c1.circumferance();
  }
}