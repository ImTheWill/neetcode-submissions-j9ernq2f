#include <iostream>
class Solution {
public:
    int getSum(int a, int b) {
        int res =0, carry = 0;
        int iA = a;
        int iB = b;
        for(int i = 0; i<32; i++){
            int tmpA = a>>i & 1;
            int tmpB = b>>i & 1;

            res |= (tmpA^tmpB^carry)<<i;
            carry = (tmpA & tmpB) | (carry & (tmpA ^ tmpB));
        }

        return res;
    }
};
