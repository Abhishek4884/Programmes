import java.io.File;
import java.util.Arrays;

public class Print_File_Names 
{
    public static void main(String[] args) 
    {
        String path = "//D:\\Java Program\\Practice";
        filename(path);
    }

    public static void filename(String path)
    {
        File file = new File(path);
        File dir[] = file.listFiles();
        Arrays.sort(dir);
        for (File e: dir) 
        {
               if(e.isFile())
               {
                System.out.println("File : " + e.getName());
               }
               else if(e.isDirectory())
               {
                System.out.println("Directory :"+ e.getName());
               }
               else
               {
                System.out.println("Not Known :" + e.getName());
               }
        }


    }
}
