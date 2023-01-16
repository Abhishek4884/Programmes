import java.util.Arrays;
import java.util.Scanner;

class Practice
{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value you want to store");
        int num = sc.nextInt();
        final int[] arr = new int[num];
        for (int i = 0;i<arr.length ; i++){
            
            System.out.println("Enter the number :");
            arr[i] = sc.nextInt();
        }

        System.out.println(Arrays.toString(arr));
        int[] res ;
        for(int num1 : arr){
            if(num1 % 2 == 0){
                res[] = num1;
            }
            
        }
        System.out.println(maxx);
    }

}