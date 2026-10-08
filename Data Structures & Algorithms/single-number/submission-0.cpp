#include <unordered_map>
#include <vector>

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::unordered_map<int, int> freqInt;

        for(int i = 0; i < nums.size(); i++){
            freqInt[nums[i]]++;
        }
        for(const auto& [num, count] : freqInt){
            if(count ==1 ){
                return num;
            }
        }
        return -1;
    }
};
