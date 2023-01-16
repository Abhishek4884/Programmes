import java.util.*;

class EvenOdd
{
  int evenodd2(int[] arr1 )
  {
	   int even = 0 ;
	   int odd = 0 ;

    for(int i : arr1)
	  {

      if(i%2==0)
	    {
	       even = even +i ;
	    }

	    else
	    {
	       odd = odd + i ;	
	    }

	  } 
        return even ;
          
        
       }

      
}



class Demo
{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);

    System.out.println("Enter the value you want to store");

     int num = sc.nextInt();

     int[] arr = new int[num];

     for(int i = 0 ; i<num;i++)
       {
	arr[i]=sc.nextInt();
       }	

	System.out.println(Arrays.toString(arr));
      
	EvenOdd ev = new EvenOdd();
	int ans = ev.evenodd2(arr);
	System.out.println(ans);

  }
}













