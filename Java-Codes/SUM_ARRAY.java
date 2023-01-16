
import java.util.Scanner;

public class SUM_ARRAY 
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
       
       
       int summ = 0;
       for (int s : arr)
       {
         summ = s+ summ; 
       }
       System.out.println(summ);

  } 
  

}
