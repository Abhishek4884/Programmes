import java.util.Arrays;
import java.util.Scanner;

 class Demo
{
     void Frequency( )
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value you want to store :");
        int num = sc.nextInt();
        int[] arr = new int[num];
        for (int i = 0; i < num; i++) 
        {
            arr[i] = sc.nextInt();    
        }
        System.out.println(Arrays.toString(arr));
        System.out.println("Enter the number you want to check freq");
        int num1 = sc.nextInt();
        int icnt = 0 ;
        for (int i : arr) 
        {
            if(i==num1)
            {
               icnt++;
            }
        }
        System.out.println(icnt);
    }
}


public class freq 
{
    public static void main(String[] args) 
    {
        Demo d = new Demo();
        d.Frequency();
        
    }
}
