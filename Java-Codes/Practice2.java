import java.util.ArrayList;
import java.util.Scanner;

class Demo
{
    public static void main(String[] args) 
    {
       ArrayList<Integer> list = new ArrayList<>(10);
       Scanner sc = new Scanner(System.in); 
       
    for (int i = 0; i < 10; i++) 
        {
            int num = sc.nextInt();
            list.add(num);            
        }
        System.out.println(list);
        ArrayList<Integer> list2 = new ArrayList<>();

        ArrayList<Integer> list3 = new ArrayList<>();

        for (int num1 :list)
        {
           for(int j = 2;j<= num1; j++ )
           {
              if(num1 % j ==0)
              {
                list3.add(num1);
                break;
              }
              else
              {
                list2.add(num1);
                break;
              }
           }
            
        }
        System.out.println(list2);
        System.out.println(list3);
    } 
}