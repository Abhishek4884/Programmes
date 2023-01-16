import java.util.ArrayList;
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
        int icnt=0;
        ArrayList<Integer> val=new ArrayList<Integer>();
        int[] arr1 = new int[num];
        for (int j = 0; j < arr.length; j++) 
        {
            if(arr[j]%2==0)
            {
              icnt++;
              val.add(arr[j]);
              arr1[j] = arr[j];
            }
        } 
        System.out.println(icnt);
        System.out.println("Arraylist"+val);
        System.out.println(Arrays.toString(arr1));


    
    }
}


 class freq2
{
    public static void main(String[] args) 
    {
        Demo d = new Demo();
        d.Frequency();
        
    }
}
