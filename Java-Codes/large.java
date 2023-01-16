
import java.util.Scanner;



class Demo
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number :");
        int a = sc.nextInt();
        System.out.println("Enter the number :");
        int b = sc.nextInt();
        System.out.println("Enter the number :");
        int c = sc.nextInt();

        int max = a ;
        if(b>max){
            max = b;
        }
        if(c>max){
            max = c;
        }
        System.out.println(max);
    }
}