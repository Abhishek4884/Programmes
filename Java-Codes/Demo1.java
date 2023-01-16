

public class Demo1
{
    public static void main(String[] args) 
    {
     
        int maxx = 0;
        int digit = 123;
        while(digit >0);
        {
            int rem = digit %10;
            if(rem > maxx)
             {
                maxx =  rem;
                // return maxx;
             }
            
            digit = digit /10;
        }
        System.out.println(maxx);
    }
   
      
}

