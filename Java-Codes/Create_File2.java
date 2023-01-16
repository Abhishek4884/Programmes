import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class Create_File2
{
    public static void main(String[] args) 
    {
            String path = "Abhi.txt";
            Createfile(path);
    }
    
    public static void Createfile(String path)
    {
        
        Scanner sc = new Scanner(System.in);
        System.out.println( "Enter the file name with extenstion");
        String name = sc.nextLine();
        FileOutputStream fos = null;
        try
        {
            fos = new FileOutputStream(name);
            System.out.println("Enter the text you want to write in file");
            String content = sc.nextLine();
            byte b[] = content.getBytes();
            fos.write(b);
            fos.close();

        }
        catch(IOException ie)
        {
            ie.printStackTrace();
        }
        finally
        {
            System.out.println("Sucess__________");
            sc.close();
        }
    }
}
