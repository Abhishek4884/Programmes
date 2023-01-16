import java.util.Scanner;

class Rev{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number :");
        int num = sc.nextInt();
        int rev = 0;
        for (int i = 0; i < num; i++) {
            rev = rev*10 +num%10;
            num = num/10;
            
        }
        System.out.println(rev);

    }
}