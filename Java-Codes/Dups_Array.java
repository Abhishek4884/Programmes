
import java.util.Scanner;

public class Dups_Array 
{
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);

    System.out.println("enter the valuess you want to store");
    int num = sc.nextInt();

    int[] arr = new int[num];

    for (int i = 0; i < num; i++) 
    {
     arr[i] = sc.nextInt(); 
    }
      
     
    for (int i = 0; i<arr.length;i++)
    {
      for (int j = i+1 ; j < arr.length; j++) 
      {
        if(arr[i]==arr[j])
        {
          System.out.println(arr[j]);
          
        }
        
      }

    }
    

  } 
  

}
