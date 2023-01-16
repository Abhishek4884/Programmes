public class prac
{
  public static void main(String[] args) 
  {
    abhi(5);
  }

  static void abhi(int i)
  {
   if(i==0){
    return;
   }
    System.out.println(i);
    abhi(i-1);

  } 
}