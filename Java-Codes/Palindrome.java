import java.util.*;

class Palindrome
{
  public static void main(String args[])
  {
   Scanner sc=new
   Scanner(System.in);
    System.out.println("Enter the first number");
    int fno=sc.nextInt();

    System.out.println("Enter the Second number");
    int sno=sc.nextInt();
    

     int temp;
     int rev;
      for(int num=fno; num<=sno; num++)
       
    {
      temp=num;
       rev=0;

       while(temp>0)
       { 
           rev= rev*10 + temp%10;
           temp = temp/10;
       }
         if(num==rev)
          System.out.println(" The number " + num + " is Palindrome");
        
         else
          System.out.println(" The number " + num + " is not Palindrome");

           
    }
  }

}