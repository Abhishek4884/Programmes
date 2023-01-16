import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

class Demo
{
    public static void main(String[] args) 
    {
        File file = new File("abhi.java");
        File opfile = new File("abhi_copy.java");
        FileInputStream fis = null;
        FileOutputStream fos = null;
        try
        {

            fis = new FileInputStream(file);
            fos = new FileOutputStream(opfile);
        }
        catch(FileNotFoundException e)
        {
            e.printStackTrace();
        }
        try
        {
            System.out.println(fis.available());

        }
        catch(IOException ie)
        {
            ie.printStackTrace();
        }
        
        int i = 0;
        try
        {
            while((i = fis.read()) !=-1 )
            {
                fos.write(i);
            }
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
        finally
        {
            if(fis!=null)
            {
                try{
                    fis.close();
                }catch(IOException ie){
                    ie.printStackTrace();
                }
                
            }
            if(fos!=null)
            {
                try{
                    fos.close();
                }catch(IOException ie){
                    ie.printStackTrace();
                }
                
            }
        }
        System.out.println("Sucessfully copied___________");

    }
}