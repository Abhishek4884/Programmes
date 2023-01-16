class CountNums{
    public static void main(String[] args) {
        int n = 1233325333;
        int res = 0;
        for (int i = 0; i < n ; i++) {
            int rem = n %10;
            if(rem == 3){
                res = res+1;
            }
            n = n/10;
        }

        System.out.println(res);
    }
}