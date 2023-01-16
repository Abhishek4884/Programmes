class Circle 

{
  double radius;

  Circle(double radius)
  {
    this.radius = radius;

  }

}

class Myclass

{
  void circumferance(Circle c)

  {
    System.out.println("circumferance of circle is" + 3.14*2*c.radius);
  }
  void area (Circle c)
  {
    System.out.println("Area of circle is" + 3.14*c.radius*c.radius);

  }
}

class Demo 
{
 public static void main(String args[])
  {
    Circle cir = new Circle(10);
    Myclass m = new Myclass();
    m.circumferance(cir);
    m.area(cir);
  }

}