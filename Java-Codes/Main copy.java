import java.util.Scanner;

class Demo{
    public static void main(String[] args) 
    {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the friut name :");
        String fruit = sc.next();
        switch (fruit)
        {
            case "Mango":
                System.out.println("King of friuts");
                break;
            case "Apple":
                System.out.println("A sweet red friut");
                break;
            case "Orange":
                System.out.println("Round friut");
                break;
            case "Grapes":
                System.out.println("Small friuts");
                break;
            default:
                System.out.println("Enter a valid friut");
        }
    }
}