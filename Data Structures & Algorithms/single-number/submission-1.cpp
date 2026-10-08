
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int unqNum = 0;
        for(int num: nums){
            unqNum ^= num;
        }
        return unqNum;
    }
};
