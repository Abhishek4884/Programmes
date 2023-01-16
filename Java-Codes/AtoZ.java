class AtoZ
{
    public static void main(String[] args) {
        String sr = "";
        for (int i = 0; i < 26; i++) 
        {
           char ch = (char)('A'+ +i);
           sr = sr+" " +ch;
           
            System.out.print(ch);
        }
        System.out.println();
        System.out.println(sr);
    }
}