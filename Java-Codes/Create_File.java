import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class Create_File 
{
    public static void main(String[] args) 
    {
            String path = "Abhi.txt";
            Createfile(path);
    }
    
    public static void Createfile(String path)
    {
        File file = new File(path);
        
        try
        {
          boolean flag =  file.createNewFile();
          if(flag)
          {
            System.out.println("File is created");
          }
          else
          {
            System.out.println("File is already present");
          }
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
        FileOutputStream fos = null;
        try
        {
            
            fos = new FileOutputStream(path);
            String str = "Abhishek";
            byte b[] = str.getBytes();
            try{
                fos.write(b);
            }
            catch(IOException ie)
            {
                ie.printStackTrace();
            }
            
        }
        catch(IOException ie)
        {
            ie.printStackTrace();
        }
        finally
        {
            try{
                fos.close();
            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }
}
