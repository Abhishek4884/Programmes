public class tp3 
{
    public static void main(String[] args) 
    {
        duplicate_Str("Abhisvaaffrthek rauaafert");
    }

    static void duplicate_Str(String str)
    {
        str = str.toLowerCase();
        char[] str1 = str.toCharArray();
        for (int i = 0; i < str.length(); i++) 
        {
           int count = 1;
            for (int j = i+1; j < str.length(); j++) 
            {
                if (str1[i]==str1[j])
                {
                    count++;
                    str1[j]='0';

                }
            }
            if(count>1 && str1[i]!='0')
            {
                System.out.println(str1[i]);
            }
 
        }
        
    }
}
