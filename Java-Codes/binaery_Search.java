public class binaery_Search 
{
  public static void main(String[] args) 
  {
    int arr [] = {1,2,3,4,5,6,7,8,9,12,45,78,96,98};
    int target = 12;
    binary(arr, target);
    
  } 
  
    static void binary(int[] arr , int target)
    {
        int start = 0;
        int end = arr.length;
        
        while(start<=end)
        {
            int mid = start + (end-start)/2 ;

            if(target < arr[mid])
            {
                end = end -1;
            }
            else if (target>arr[mid])
            {
                start = start+1;
            }
            else
            {
                System.out.println("Tareget  hit");
                break;
            }
           
        }
        
    }
}
