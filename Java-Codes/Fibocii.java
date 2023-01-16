import java.util.Scanner;

class Fiboncii{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number :");
        int i = sc.nextInt();
        
        int a = 0;
        int b = 1;


        for (int cout = 1; cout < i ; cout++) {
            int temp = b;
            b = b + a;
            a=temp;

            System.out.print(","+b);
            
        }
         
    }
}