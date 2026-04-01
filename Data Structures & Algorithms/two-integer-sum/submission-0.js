class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashMap = new Map();// use HashMap instead of HashSet to allow for us to get a key pair

        //we are looking for the nums difference between target and the current num
        for(let i = 0; i < nums.length; i++){
            let difference = target - nums[i]
            if(hashMap.has(difference)){
                return [hashMap.get(difference), i]
            }else{
                hashMap.set(nums[i],i)
            }
        }





    }
}
