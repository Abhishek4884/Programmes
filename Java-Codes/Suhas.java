class Box
{
  double width, length ,height;
  Box(double width, double length, double height)
   {
    this.width=width;
    this.length=length;
    this.height=height; 
   }

}

class Myclass
{
   void volume(Box b)
  {
   System.out.println("Volume of Box " + b.width*b.height*b.length);   
  }

}
class Suhas
{
  public static void main(String args[])
  {
   Box c= new Box(10,11,12);
   Myclass m = new Myclass();
    m.volume(c);
  }


}