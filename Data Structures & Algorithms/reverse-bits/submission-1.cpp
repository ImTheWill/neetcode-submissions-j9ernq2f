class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int start = 31, end = 0;
        uint32_t res = n;
        while(start> end){
            int tempStart = ((res>>start) & 1);
            int tempEnd = ((res>>end ) & 1);

            if(tempStart != tempEnd){
                res ^= (1U<<start);
                res ^= (1U<<end);
                //toggles the bit if they are different
                //
            }
            start--;
            end++;

        }
        return res;
    }
};
