
import java.io.FileInputStream;
import java.io.IOException;

public class read_file 
{
    public static void main(String[] args) 
    {
        String path = "abhi.java";
        readfile(path);
    }

    public static void readfile(String path)
    {
        
        FileInputStream fis = null;
        try 
        {
            fis = new FileInputStream(path);
            int c =0;
            while((c=fis.read())!=-1)
            {
                System.out.print((char)c);
            }
        } 
        catch (IOException e) 
        {
            e.printStackTrace();
        }
        finally
        {
            try {
                fis.close();
            } catch (IOException e) {
                
                e.printStackTrace();
            }
        }
    }
}
