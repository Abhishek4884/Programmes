import java.util.Scanner;

class String_Pallin
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string :");
        String str = sc.nextLine();
        System.out.println(ispallin(str));
    }

    static boolean ispallin(String str)
    {
        str = str.toLowerCase();

        
        for (int i = 0; i <str.length(); i++) 
        {
            char start = str.charAt(i);
            char end = str.charAt(str.length()-1-i);
            // System.out.print(end);
            if(start != end)
            {
                return false;
            }
                        
        }
        return true;
    }
} 