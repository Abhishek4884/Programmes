import java.util.Scanner;
 
class Demo
{
    boolean Reverse(String Str)
    {
        String new_str = "";
        String temp = Str;
        for (int i = 0; i < temp.length(); i++) 
        {
            char ch = temp.charAt(i);
            new_str = ch + new_str;    
        }
        System.out.println(new_str);
        if(new_str.equals(Str))
        {
           return true;
        }
        else
        {
            return false;
        }
        
    }
   
}


public class RevStr2 
{
 public static void main(String[] args) 
 {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the string :");
    String Str = sc.nextLine();
    Demo d = new Demo();
    boolean b = d.Reverse(Str);
    System.out.println(b);
    

 }    
}
