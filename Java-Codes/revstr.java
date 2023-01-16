import java.util.Scanner;

class Str
{
  void rev()
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the string ");
    String s = sc.nextLine();
    String t = "";
    for (int i = 0; i < s.length(); i++) 
    {
        char ch = s.charAt(i);
        t = ch + t ;    
    }
    System.out.println(t);
  }
}


public class revstr
{
    public static void main(String[] args) 
    {
        Str st = new Str();
        st.rev();
    }
}