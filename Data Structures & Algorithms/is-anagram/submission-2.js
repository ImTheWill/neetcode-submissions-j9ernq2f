class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length!== t.length){
            return false;
        }

        const countS = {};
        const countT = {};

        for (let i = 0; i < s.length; i++){
            countS[s[i]] = 1 + (countS[s[i]]|| 0);
            countT[t[i]] = 1 + (countT[t[i]] || 0)
        }

        //for every field/key in countS we access and get its value 
        //and do the same with countT if they have the same amount then they are anagrams
        for (const key in countS){
            if(countS[key] !== countT[key]){
                return false;
            }
        }

        return true;

    }
}
