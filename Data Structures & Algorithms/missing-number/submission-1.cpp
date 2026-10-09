#include <algorithm>

class Solution {
public:
    int missingNumber(vector<int>& nums){
        //n = arr.size()
        int res = 0;
        for(int i = 0; i < nums.size(); i++){
            res ^= nums[i];
        }

        for(int i = 0; i < nums.size()+1; i++){
            res ^= i;
        }
        
        return res;
    }
};
