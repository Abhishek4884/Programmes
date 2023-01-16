 class Thread_2 extends Thread
{

    synchronized public void run()
    {
        for (int i = 0; i <= 10; i++) 
        {
          System.out.println(getName()+" :"+i);    
        }
    }
}

class Thread_3 extends Thread
{
    synchronized public void run()
    {
        for (int i = 0; i <= 10; i++) 
        {
          System.out.println(getName()+" :"+i);    
        }
    }
}

public class Thread_1
{
    public static void main(String[] args) 
    {
        try 
        {
            Thread_2 t = new Thread_2();
            t.setName("Abhi");
            t.start();
            t.join();
             
            Thread_3 t3 = new Thread_3();
            t3.setName("Adesh");
            t3.start();
            t3.join();
              
        } 
        catch (Exception e) 
        {
            e.printStackTrace();
        }
          
             
        
    }
}

