


class Demo2 extends Thread
{
    public void run()
    {
        for (int i = 0; i < 5; i++) {
            System.out.println("Class Demo2 :"+i);
        }
    }
}

class Demo extends Thread
{
    public void run()
    {
        for (int i = 0; i < 5; i++) {
            System.out.println("Class Demo :"+i);
        }
    }
}

public class Threading
{
    public static void main(String[] args) {
        Demo2 d2 = new Demo2();
        d2.start();

        Demo d = new Demo();
        d.start();
    }
}