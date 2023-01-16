class Box 
{  
  double width , height , length ;

  Box(double width ,double height , double length)
  {
   this.width=width;
   this.height=height;
   this.length=length; 
  }
   void volume()
  {
   System.out.println("Volume of Box" + width*height*length);

  }

}

class First

{
  Box meth()
  {
   Box f = new Box(10,11,12);
   return f;
  }
}

class Demo
{
  public static void main(String args[])

  {
    First f1 = new First();
    Box b1 ;
      b1= f1.meth();
      b1.volume();
  }
}