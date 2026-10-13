class Solution {
public:
    int reverse(int x) {
        const int max = 2147483647;
        const int min = -2147483648;

        int res = 0;
        while(x!=0){
            int num = x%10;
            x /= 10;
            if(res > max/10 || (res == max/10 && num >max%10)){
                return 0;
            }else if(res < min/10 || (res == min/10 && num <min%10)){
                return 0;
            }else{
                res = res*10 + num;
            }
        }
        return res;

    }
};
