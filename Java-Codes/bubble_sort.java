

public class bubble_sort 
{
    public static void main(String[] args) 
    {
        int arr [] = {10,25,8,74,12,53,32,3,1,25};
        
        int ans = sort(arr);
        System.out.println(ans);
    }

    static int sort(int[] arr)
    {
        for (int i = 0; i < arr.length; i++) 
        {
              for (int j = i+1; j < arr.length; j++) 
              {
                 if(arr[i]>arr[j])
                 {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j]= temp;
                 }
              }
        }
        return arr[arr.length-2];
    }
}
