#include <algorithm>

class Solution {
public:
    int missingNumber(vector<int>& nums){
        //n = arr.size()
        int res = nums.size();
        for(int i = 0; i < nums.size(); i++){
            res ^= i ^ nums[i];
        }
        
        return res;
    }
};
