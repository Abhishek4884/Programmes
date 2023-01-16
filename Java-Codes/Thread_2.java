public class Thread_2 extends Thread
{
    public synchronized void run()
    {
       System.out.println("Hello");
    }

    public static void main(String[] args) 
    {
        try
        {
            for (int i = 0; i < 10; i++) {
                System.out.println("Main Thraed");
            }
        }
        finally
        {
            
        }

        
       
        Thread_2 t2 = new Thread_2();

        t2.run();
        t2.start();
    }
}
