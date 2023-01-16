class Palindrome
{

public static void main(String args[])
{
int r;

int sum=0;

int temp;

int n=45; temp=n;

while(n>0)

{   
r=n%10;

  sum (sum*10)+r;
  n=n/10;
}
   if(temp==sum)

   System.out.println("Palindrome number");

   else

   System.out.println("Not a Palindrome number");